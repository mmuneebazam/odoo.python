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
