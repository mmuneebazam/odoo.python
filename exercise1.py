price = 1500.0
quantity = 3
discount_percent = 10

total_before_discount = price * quantity
discount_amount = total_before_discount * (discount_percent / 100)
final_price = total_before_discount - discount_amount
if final_price > 1000:
    print("Final price is above 1000")
else:
    print("Final price is 1000 or below")
