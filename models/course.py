from odoo import models, fields
class Courses(models.Model):
    _name = 'todos.course'
    _description = 'Courses INFO'

    name = fields.Char()
    department_id = fields.Many2one('todos.department', string="Department", ondelete="cascade")
