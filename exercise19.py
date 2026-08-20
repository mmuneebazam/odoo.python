# ============================================================
# COMPUTED FIELDS AND @api.depends
# ============================================================

from odoo import models, fields, api


class TrainingCourse(models.Model):
    _name = "training.course"
    _description = "Training Course"

    name = fields.Char(string="Course Name")

    # Original course price
    price = fields.Float(string="Price")

    # Discount percentage
    discount = fields.Float(string="Discount (%)")

    # Computed field
    # The value is calculated automatically from price and discount.
    # store=True means the calculated value is stored in the database.
    total_price = fields.Float(
        string="Total Price",
        compute="_compute_total_price",
        store=True,
    )

    # @api.depends tells Odoo which fields affect the computation.
    # If price or discount changes, Odoo recalculates total_price.
    @api.depends("price", "discount")
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.price * (
                1 - record.discount / 100
            )


# ============================================================
# EXAMPLE
# ============================================================

# Price = 1000
# Discount = 20%
#
# Calculation:
#
# total_price = 1000 * (1 - 20 / 100)
# total_price = 1000 * 0.80
# total_price = 800
#
# If price or discount changes,
# Odoo automatically recalculates total_price.
