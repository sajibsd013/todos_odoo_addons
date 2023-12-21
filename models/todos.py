from odoo import models, fields

class Todos(models.Model):
    _name = 'todos.todo'
    _description = 'ToDos'

    name = fields.Char()
    is_completed = fields.Boolean()
