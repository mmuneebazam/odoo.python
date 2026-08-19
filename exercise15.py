from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(
        string='Student Name',
        required=True
    )

    class_id = fields.Many2one(
        'school.class',
        string='Main Class'
    )

    course_ids = fields.Many2many(
        'school.course',
        string='Extracurricular Courses'
    )
