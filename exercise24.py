# ============================================================
# 23. LAMBDA FUNCTIONS, FILTERED AND MAPPED
# ============================================================

from odoo import models, fields


class TrainingStudent(models.Model):
    _name = "training.student"
    _description = "Training Student"

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")

    def exercise_lambda_filtered_mapped(self):

        # ----------------------------------------------------
        # Get all students
        # ----------------------------------------------------
        students = self.env["training.student"].search([])

        # ----------------------------------------------------
        # Use filtered() with lambda
        # Keep only students older than 18
        # ----------------------------------------------------
        adult_students = students.filtered(
            lambda student: student.age > 18
        )

        # ----------------------------------------------------
        # Use mapped()
        # Get the names of adult students
        # ----------------------------------------------------
        student_names = adult_students.mapped("name")

        # ----------------------------------------------------
        # Print results
        # ----------------------------------------------------
        print("Students older than 18:")

        for student in adult_students:
            print(student.name, "-", student.age)

        print("Adult Student Names:", student_names)


# ============================================================
# HOW IT WORKS
# ============================================================

# All Students
#      ↓
# filtered()
#      ↓
# lambda student: student.age > 18
#      ↓
# Students older than 18
#      ↓
# mapped("name")
#      ↓
# Names of those students


# ============================================================
# QUICK REFERENCE
# ============================================================

# Lambda:
# Small anonymous function
#
# lambda student: student.age > 18


# filtered():
# Filters records based on a condition
#
# students.filtered(lambda student: student.age > 18)


# mapped():
# Gets a field/value from each record
#
# students.mapped("name")


# ============================================================
# WHY IS mapped() CONVENIENT?
# ============================================================

# mapped() is convenient because it gets the required field
# values from all records in one operation without writing
# a manual loop.
