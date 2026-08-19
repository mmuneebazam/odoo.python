from odoo import models, fields


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'

    name = fields.Char(
        string='Course Name',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    duration = fields.Float(
        string='Duration (Hours)'
    )

    price = fields.Float(
        string='Price'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('done', 'Done'),
        ],
        string='State',
        default='draft'
    )
