students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 21},
]

students_sorted_by_age = []

for student in students:
    if student["age"] not in students.keys():
        students_sorted_by_age[student["age"]] = student["name"]
    else:
        students_sorted_by_age[student["age"]].append(student["name"])

print(students_sorted_by_age)
