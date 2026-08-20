# ============================================================
# 22. CONTEXT
# ============================================================

from odoo import models


class TrainingCourse(models.Model):
    _name = "training.course"
    _description = "Training Course"

    def exercise_context(self):

        # ----------------------------------------------------
        # 1. Read the current context
        # ----------------------------------------------------
        context = self.env.context

        print("Current Context:", context)

        # ----------------------------------------------------
        # 2. Check a specific value from the context
        # ----------------------------------------------------
        if self.env.context.get("from_import"):
            print("This operation is coming from an import.")
        else:
            print("This operation is not from an import.")

        # ----------------------------------------------------
        # 3. Add custom information to the context
        # ----------------------------------------------------
        records = self.with_context(
            skip_notification=True
        )

        # ----------------------------------------------------
        # 4. Read the new context value
        # ----------------------------------------------------
        if records.env.context.get("skip_notification"):
            print("Notification should be skipped.")


# ============================================================
# CONTEXT WITH MULTIPLE VALUES
# ============================================================

# You can pass multiple values using with_context():

# records = self.with_context(
#     from_import=True,
#     skip_notification=True,
# )


# ============================================================
# CONTEXT EXAMPLES
# ============================================================

# Read context:
# self.env.context

# Get a specific value:
# self.env.context.get("from_import")

# Add a value to context:
# self.with_context(from_import=True)

# Add multiple values:
# self.with_context(
#     from_import=True,
#     skip_notification=True,
# )


# ============================================================
# HOW CONTEXT WORKS
# ============================================================

# self
#   ↓
# self.env
#   ↓
# self.env.context
#   ↓
# Read extra information
#   ↓
# Context-based behavior


# with_context()
#       ↓
# Add extra information
#       ↓
# self.with_context(from_import=True)
#       ↓
# Context carries the information
#       ↓
# Code checks the context
#       ↓
# Special behavior


# ============================================================
# KEY CONCEPT
# ============================================================

# Context = Extra information/instructions passed
# through Odoo ORM operations.
#
# self.env.context
#     → Read current context
#
# context.get("key")
#     → Read a specific context value
#
# with_context(key=value)
#     → Add/pass custom context information
