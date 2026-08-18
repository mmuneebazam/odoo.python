from odoo import models, fields


class TrainingStudent(models.Model):
    _name = "training.student"
    _description = "Training Student"

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")

    def print_student_names(self):
        for record in self:
            print(record.name)
