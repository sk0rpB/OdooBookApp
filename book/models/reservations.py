from odoo import models, fields
from datetime import date

class Book(models.Model):
    _name = 'book.issue'
    _description = 'Book issue record'

    contact_id = fields.Many2one('res.partner', string="Contact", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date")
    book_ids = fields.Many2many('book', string="Books", required=True)
    status = fields.Selection(
        [('reserved', 'Reserved'), ('issued', 'Issued'), ('returned', 'Returned'), ('cancelled', 'Cancelled')],
        string="Status",
        default='reserved',
        required=True
    )

    def check_overdue_books(self):
        today = date.today()
        
        overdue = self.search([('status', '=', 'issued'), ('end_date', '<', today)])
        
        for issue in overdue:
            self.send_reminder(issue)

    def send_reminder(self, issue):
        template = self.env.ref('book.book_mail_template')
        if template:
            template.send_mail(issue, force_send=True)