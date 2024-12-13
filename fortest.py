students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 21},
]

students_sorted = {}

for student in students:
    if student["age"] in students_sorted:
        students_sorted.append[student["name"]]
    else:
        students_sorted[student["age"]] = [student["name"]]

print(students_sorted)
