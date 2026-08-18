def calculate_tax(amount, tax_rate):
    tax = amount * (tax_rate / 100)
    return tax

def calculate_total_with_tax(amount, tax_rate):
    tax = calculate_tax(amount, tax_rate)
    total = amount + tax
    return total

# Test 1
amount1 = 1000
tax_rate1 = 15
print(calculate_tax(amount1, tax_rate1))
print(calculate_total_with_tax(amount1, tax_rate1))

# Test 2
amount2 = 2500
tax_rate2 = 8
print(calculate_tax(amount2, tax_rate2))
print(calculate_total_with_tax(amount2, tax_rate2))
