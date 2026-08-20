# ============================================================
# @api.onchange EXERCISE
# ============================================================

from odoo import models, fields, api


class TrainingRegistration(models.Model):
    _name = "training.registration"
    _description = "Training Registration"

    name = fields.Char(string="Registration Name")

    # Selected training course
    course_id = fields.Many2one(
        "training.course",
        string="Course"
    )

    # Duration taken from the selected course
    suggested_duration = fields.Float(
        string="Suggested Duration"
    )

    # When the course changes in the form,
    # automatically set the suggested duration.
    @api.onchange("course_id")
    def _onchange_course_id(self):
        if self.course_id:
            self.suggested_duration = self.course_id.duration
        else:
            self.suggested_duration = 0.0


# ============================================================
# HOW IT WORKS
# ============================================================

# User selects a course
#        ↓
# @api.onchange("course_id")
#        ↓
# Course selected?
#        ↓
#       YES
#        ↓
# self.course_id.duration
#        ↓
# suggested_duration
#
# Example:
#
# Course: Python Odoo Training
# Duration: 30 hours
#
# User selects course
#        ↓
# Suggested Duration = 30 hours
