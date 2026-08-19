from odoo import models


class RecordsetExercise(models.Model):
    _name = "recordset.exercise"
    _description = "Recordset Exercise"

    def exercise_recordsets(self):
        # Search for all active partners
        partners = self.env["res.partner"].search([
            ("active", "=", True)
        ])

        # Loop through the recordset and print partner names
        for partner in partners:
            print("Active Partner:", partner.name)

        # Filter partners whose names contain the letter 'a'
        filtered_partners = partners.filtered(
            lambda p: "a" in p.name.lower()
        )

        # Print filtered partner names
        for partner in filtered_partners:
            print("Partner with 'a':", partner.name)





# Recordsets in Odoo
# What is a Recordset?

# An Odoo recordset is a collection of records belonging to the same model.

# For example, a recordset of res.partner can contain multiple contact records.

# Why Recordsets Matter

# Recordsets are an important part of Odoo development because Odoo's ORM works with collections of records rather than only individual records.

# A recordset can be:

# Empty
# A single record
# Multiple records

# This is why a method's self should not automatically be assumed to contain only one record.

# Common Recordset Operations
# Search

# search() is used to retrieve records from an Odoo model. It returns a recordset.

# Iteration

# A recordset can be iterated through to process each record individually.

# Filtering

# filtered() is used to create a new recordset containing only records that satisfy a specific condition.

# Important Concept: self

# In Odoo, self represents the current recordset.

# It does not necessarily mean one record. It can contain one or multiple records.

# Therefore, Odoo methods should be written with the possibility that self contains multiple records.

# Key Takeaway

# Recordset = same model ke multiple Odoo records ka collection.

# Recordsets allow developers to:

# Retrieve records
# Iterate through records
# Filter records
# Map data
# Perform ORM operations

# The recordset-based approach is one of the important differences between normal Python programming and Odoo development.
