numbers = [5, 12, 8, 25, 30]

# First loop - print only numbers greater than 10
for num in numbers:
    if num > 10:
        print(num)

# Second loop - calculate the total
total = 0
for num in numbers:
    total = total + num

print("Total:", total)
