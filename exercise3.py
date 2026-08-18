# Dictionary with three products and prices
prices = {"Laptop": 1200, "Mouse": 25, "Keyboard": 70}

# Loop through dictionary and print each product with price
for product, price in prices.items():
    print(product, price)

# List with duplicate product names
product_list = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Mouse"]

# Convert to set to remove duplicates
unique_products = set(product_list)
print(unique_products)
