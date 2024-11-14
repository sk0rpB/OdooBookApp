from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def get_book_issues(self):
        book_issues = self.env['book.issue'].search([('contact_id', '=', self.id)])
        issue_data = []

        for issue in book_issues:
            issue_data.append({
                'book_title': issue.book_id.name,
                'start_date': issue.start_date,
                'end_date': issue.end_date,
                'status': issue.status,
            })
        return issue_data