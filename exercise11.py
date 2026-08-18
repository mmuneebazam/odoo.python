def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return quantity


# Test with try/except
try:
    validate_quantity(5)
    print("Quantity 5 is valid")

    validate_quantity(-2)
    print("This line will not run")

except ValueError as e:
    print(f"Error: {e}")
    print("Please enter a valid quantity greater than zero.")
