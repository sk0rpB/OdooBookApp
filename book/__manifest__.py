{
    'name': 'Book',
    'version': '1.0',
    'category': 'Book',
    'summary': 'Module to manage books',
    'description': 'A module to register books with title, description, pages, and genres.',
    'author': 'Modestas',
    'depends': ['base'],
    'data': [
        'views/book_view.xml',
        # 'views/email.xml',
        # 'views/ir_crons.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}