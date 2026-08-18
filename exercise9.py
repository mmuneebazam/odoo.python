class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class SpecialProduct(BaseProduct):
    def get_price(self):
        base_price = super().get_price()
        return base_price * 1.10


# Test
product1 = BaseProduct("Laptop", 1000)
product2 = SpecialProduct("Premium Laptop", 1000)

print(product1.get_price())
print(product2.get_price())
