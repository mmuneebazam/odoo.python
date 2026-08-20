# ============================================================
# 22. ENVIRONMENT: self.env
# ============================================================

from odoo import models


class TrainingCourse(models.Model):
    _name = "training.course"
    _description = "Training Course"

    def exercise_environment(self):

        # ----------------------------------------------------
        # 1. Access the current user
        # ----------------------------------------------------
        user = self.env.user

        # ----------------------------------------------------
        # 2. Access the current company
        # ----------------------------------------------------
        company = self.env.company

        # ----------------------------------------------------
        # 3. Access another Odoo model using self.env
        # ----------------------------------------------------
        Partner = self.env["res.partner"]

        # ----------------------------------------------------
        # 4. Find all active partners
        # ----------------------------------------------------
        active_partners = Partner.search([
            ("active", "=", True)
        ])

        # ----------------------------------------------------
        # 5. Print current user's name
        # ----------------------------------------------------
        print("Current User:", user.name)

        # ----------------------------------------------------
        # 6. Print current company's name
        # ----------------------------------------------------
        print("Current Company:", company.name)

        # ----------------------------------------------------
        # 7. Print number of active partners
        # ----------------------------------------------------
        print("Number of Active Partners:", len(active_partners))


# ============================================================
# HOW self.env WORKS
# ============================================================

# self
#   ↓
# Current Model / Recordset
#   ↓
# self.env
#   ↓
# Odoo Environment
#   │
#   ├── self.env.user
#   │      ↓
#   │   Current User
#   │
#   ├── self.env.company
#   │      ↓
#   │   Current Company
#   │
#   └── self.env["res.partner"]
#          ↓
#       res.partner Model
#          ↓
#       search()
#          ↓
#       Active Partners
#
# ============================================================
# KEY CONCEPT
# ============================================================
#
# self.env is the bridge between the current Odoo model
# and the rest of the Odoo application.
#
# self.env["model.name"] → Access another model
# self.env.user          → Current user
# self.env.company       → Current company
# self.env.context       → Current context
# self.env.cr             → Database cursor
#
# ============================================================
