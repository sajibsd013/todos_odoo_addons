from odoo import models, fields

class Department(models.Model):
    _name = 'todos.department'
    _description = 'Department INFO'

    name = fields.Char()
