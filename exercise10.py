def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def calculate_invoice_total(amount, tax_rate):
    tax = amount * (tax_rate / 100)
    return amount + tax


# Test
print(calculate_invoice_total(1000, 15))
print(calculate_invoice_total(2500, 8))
