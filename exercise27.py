# 27. Defaults and Default Functions

from odoo import models, fields


class TrainingCourse(models.Model):
    _name = "training.course"
    _description = "Training Course"

    name = fields.Char(string="Course Name")

    # Default value is "draft"
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
        ],
        default="draft",
    )

    # Default function
    def _default_company(self):
        return self.env.company

    # Automatically uses the current company
    company_id = fields.Many2one(
        "res.company",
        default=_default_company,
    )
