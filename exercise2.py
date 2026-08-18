 

order_name = "SO0123"
customer_name = "NUST"
total_amount = 4050.0

message_fstring = f"Order {order_name} for {customer_name}, total amount {total_amount}"
message_concat = "Order " + order_name + " for " + customer_name + ", total amount " + str(total_amount)

print(message_fstring)
print(message_concat)
