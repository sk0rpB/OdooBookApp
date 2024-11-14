from odoo import models, fields

class Book(models.Model):
    _name = 'book'
    _description = 'Book'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Short Description")
    pages = fields.Integer(string="Number of Pages")
    genre_ids = fields.Many2many('book.genre', string="Genres")