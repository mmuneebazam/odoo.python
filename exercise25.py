# 25. List Comprehensions

students = [
    {"name": "Ali", "active": True},
    {"name": "Ahmed", "active": False},
    {"name": "Sara", "active": True},
    {"name": "Hassan", "active": False},
]


# List Comprehension
active_names = [
    student["name"]
    for student in students
    if student["active"]
]

print(active_names)


# Normal For Loop
active_names = []

for student in students:
    if student["active"]:
        active_names.append(student["name"])

print(active_names)


# Both give:
# ['Ali', 'Sara']
