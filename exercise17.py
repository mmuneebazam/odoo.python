from odoo import models


class ORMExercise(models.Model):
    _name = "orm.exercise"
    _description = "ORM Exercise"


    def exercise_orm_methods(self):
        Partner = self.env["res.partner"]

        # 1. SEARCH
        # Find customers from a chosen country
        customers = Partner.search([
            ("country_id.name", "=", "Pakistan"),
            ("customer_rank", ">", 0),
        ])

        for customer in customers:
            print("Customer:", customer.name)

        # 2. BROWSE
        # Get a customer record using its ID
        customer = Partner.browse(10)

        if customer.exists():
            print("Browsed Customer:", customer.name)

            # 3. WRITE
            # Update a field on the customer
            customer.write({
                "email": "updated@example.com",
            })

            print("Customer email updated:", customer.email)

        # 4. CREATE
        # Create a new customer
        new_customer = Partner.create({
            "name": "ORM Exercise Customer",
            "email": "customer@example.com",
            "customer_rank": 1,
        })

        print("New Customer Created:", new_customer.name)

        # 5. UNLINK
        # Delete the newly created customer
        # Uncomment the following line if you want to test unlink()
        # new_customer.unlink()
