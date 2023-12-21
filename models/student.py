from odoo import models, fields
class Student(models.Model):
    _name = 'todos.students'
    _description = 'Student INFO'

    name = fields.Char()
    regi_no = fields.Char()
    mobile = fields.Char()
    department_id = fields.Many2one('todos.department', string="Department", ondelete="cascade")
    course_ids = fields.Many2many('todos.course', string="Course", ondelete="cascade")
