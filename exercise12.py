# utils.py:

def calculate_total(price, quantity):
    return price * quantity

# main.py:

from utils import calculate_total

total = calculate_total(price=250, quantity=4)
print(f"Total price: {total}")
