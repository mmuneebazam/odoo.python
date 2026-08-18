class Customer:
    def __init__(self, name, credit_limit):
        self.name = name
        self.credit_limit = credit_limit

    def can_afford(self, order_amount):
        return order_amount <= self.credit_limit

# Test
customer1 = Customer("Ali Traders", 5000)
customer2 = Customer("Sara Enterprises", 1000)

print(customer1.can_afford(3000))
print(customer1.can_afford(6000))
print(customer2.can_afford(1000))
