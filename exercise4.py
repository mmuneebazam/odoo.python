order_amount = 2500
customer_is_company = True

if order_amount >= 2000 and customer_is_company:
    discount = 15
elif order_amount >= 1000:
    discount = 10
else:
    discount = 0

print(discount)
