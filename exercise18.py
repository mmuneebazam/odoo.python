# ============================================================
# SEARCH DOMAINS
# ============================================================

from odoo import models


class SearchDomainExercise(models.Model):
    _name = "search.domain.exercise"
    _description = "Search Domain Exercise"

    def exercise_search_domains(self):

        Partner = self.env["res.partner"]

        # ----------------------------------------------------
        # 1. Basic Domain
        # Find all active partners
        # ----------------------------------------------------
        active_partners = Partner.search([
            ("active", "=", True),
        ])

        for partner in active_partners:
            print("Active Partner:", partner.name)

        # ----------------------------------------------------
        # 2. Multiple Conditions (AND)
        # Find active companies
        # Both conditions must be True
        # ----------------------------------------------------
        companies = Partner.search([
            ("active", "=", True),
            ("is_company", "=", True),
        ])

        for company in companies:
            print("Active Company:", company.name)

        # ----------------------------------------------------
        # 3. Text Search using ilike
        # Find partners whose name contains "ali"
        # ----------------------------------------------------
        ali_partners = Partner.search([
            ("name", "ilike", "ali"),
        ])

        for partner in ali_partners:
            print("Partner containing 'ali':", partner.name)

        # ----------------------------------------------------
        # 4. Comparison Operator
        # Find customers whose customer_rank is greater than 0
        # ----------------------------------------------------
        customers = Partner.search([
            ("customer_rank", ">", 0),
        ])

        for customer in customers:
            print("Customer:", customer.name)

        # ----------------------------------------------------
        # 5. Relational Field Domain
        # Find partners from Pakistan
        # ----------------------------------------------------
        pakistan_partners = Partner.search([
            ("country_id.name", "=", "Pakistan"),
        ])

        for partner in pakistan_partners:
            print("Pakistan Partner:", partner.name)

        # ----------------------------------------------------
        # 6. OR Operator (|)
        # Find partners who are either companies OR customers
        # ----------------------------------------------------
        companies_or_customers = Partner.search([
            "|",
            ("is_company", "=", True),
            ("customer_rank", ">", 0),
        ])

        for partner in companies_or_customers:
            print("Company or Customer:", partner.name)

        # ----------------------------------------------------
        # 7. NOT Equal (!=)
        # Find partners who are not companies
        # ----------------------------------------------------
        non_companies = Partner.search([
            ("is_company", "!=", True),
        ])

        for partner in non_companies:
            print("Non Company:", partner.name)

        # ----------------------------------------------------
        # 8. Combined Domain
        # Find active customers from Pakistan
        # ----------------------------------------------------
        pakistan_customers = Partner.search([
            ("active", "=", True),
            ("country_id.name", "=", "Pakistan"),
            ("customer_rank", ">", 0),
        ])

        for customer in pakistan_customers:
            print("Pakistan Customer:", customer.name)

        # ----------------------------------------------------
        # 9. Limit
        # Find only the first 5 active partners
        # ----------------------------------------------------
        first_five = Partner.search(
            [("active", "=", True)],
            limit=5,
        )

        for partner in first_five:
            print("First Five:", partner.name)

        # ----------------------------------------------------
        # 10. Order
        # Find active partners ordered by name
        # ----------------------------------------------------
        ordered_partners = Partner.search(
            [("active", "=", True)],
            order="name asc",
        )

        for partner in ordered_partners:
            print("Ordered Partner:", partner.name)


# ============================================================
# DOMAIN QUICK REFERENCE
# ============================================================

# Basic structure:
# ("field", "operator", value)

# Equal:
# ("active", "=", True)

# Not Equal:
# ("active", "!=", False)

# Greater Than:
# ("customer_rank", ">", 0)

# Less Than:
# ("customer_rank", "<", 10)

# Greater Than or Equal:
# ("customer_rank", ">=", 1)

# Less Than or Equal:
# ("customer_rank", "<=", 10)

# Text Search:
# ("name", "ilike", "ali")

# Multiple conditions = AND:
# [
#     ("active", "=", True),
#     ("is_company", "=", True),
# ]

# OR:
# [
#     "|",
#     ("is_company", "=", True),
#     ("customer_rank", ">", 0),
# ]

# NOT:
# [
#     "!",
#     ("is_company", "=", True),
# ]

# Relational field:
# ("country_id.name", "=", "Pakistan")
