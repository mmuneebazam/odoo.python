def show_details(*args, **kwargs):
    print(args)
    print(kwargs)

# Test 1
show_details("Laptop", "Mouse", price=1200, discount=10)

# Test 2
show_details(1, 2, 3, category="Electronics", in_stock=True)
