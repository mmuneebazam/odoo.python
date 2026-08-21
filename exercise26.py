# 26. Properties of Odoo Record Fields and Related Fields

from odoo import models, fields


class TrainingCourse(models.Model):
    _name = "training.course"
    _description = "Training Course"

    name = fields.Char(string="Course Name")

    product_id = fields.Many2one(
        "product.product",
        string="Product",
    )

    product_category_id = fields.Many2one(
        related="product_id.categ_id",
        store=True,
        string="Product Category",
    )


# Related Field:
# product_id.categ_id
#        ↓
# product_category_id
#
# It gets the category from the selected product.
#
# store=True:
# The related value is also stored in the database.
