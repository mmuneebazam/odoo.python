# ============================================================
# 21. @api.constrains AND VALIDATION
# ============================================================

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainingStudent(models.Model):
    _name = "training.student"
    _description = "Training Student"

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")

    # @api.constrains is used to enforce business rules.
    # This method runs when the "age" field is created or updated.
    @api.constrains("age")
    def _check_age(self):
        for record in self:
            if record.age < 16:
                raise ValidationError(
                    "Student must be at least 16 years old."
                )


# ============================================================
# HOW IT WORKS
# ============================================================

# Student Age
#     ↓
# @api.constrains("age")
#     ↓
# _check_age()
#     ↓
# Is age less than 16?
#     ↓
# ┌───────────────┬────────────────┐
# │               │                │
# ▼               ▼                │
# YES             NO               │
# │               │                │
# ▼               ▼                │
# ValidationError  Valid            │
# │               │                │
# ▼               ▼                │
# Record rejected  Continue         │
#                                  │
# ============================================================
# IMPORTANT:
#
# @api.constrains → Server-side business validation
#
# ValidationError → Stops invalid data from being saved
#
# Example:
# age = 14
# → ValidationError
#
# age = 18
# → Valid
# ============================================================
