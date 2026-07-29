# =====================================================
# PYTHON COLLECTIONS
# =====================================================

print("=" * 50)
print("Python Collections")
print("=" * 50)


# =====================================================
# 1. LIST
# =====================================================

print("1. List")

students = ["Moin", "Aamir", "Yasin", "Adil"]

print(students)
print(type(students))


# =====================================================
# 2. TUPLE
# =====================================================

print("2. Tuple")

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))


# =====================================================
# 3. SET
# =====================================================

print("3. Set")

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# =====================================================
# 4. DICTIONARY
# =====================================================

print("4. Dictionary")

student = {
    "name": "Moin",
    "age": 32,
    "city": "Ahmedabad"
}

print(student)
print(type(student))


# =====================================================
# 5. ACCESS LIST ITEMS
# =====================================================

print("5. Access List Items")

print(students[0])
print(students[1])
print(students[-1])


# =====================================================
# 6. ACCESS TUPLE ITEMS
# =====================================================

print("6. Access Tuple Items")

print(colors[0])
print(colors[2])


# =====================================================
# 7. ACCESS DICTIONARY VALUES
# =====================================================

print("7. Access Dictionary Values")

print(student["name"])
print(student["age"])
print(student["city"])


# =====================================================
# 8. COLLECTION LENGTH
# =====================================================

print("8. Collection Length")

print(len(students))
print(len(colors))
print(len(numbers))
print(len(student))


# =====================================================
# 9. COLLECTION INDEXING
# =====================================================

print("9. Collection Indexing")

print(students[2])
print(colors[1])


# =====================================================
# 10. COLLECTION SLICING
# =====================================================

print("10. Collection Slicing")

print(students[0:2])
print(students[1:4])
print(colors[0:2])


# =====================================================
# 11. NESTED LIST
# =====================================================

print("11. Nested List")

marks = [
    [85, 90],
    [78, 82],
    [95, 88]
]

print(marks)
print(marks[0])
print(marks[0][1])


# =====================================================
# 12. NESTED DICTIONARY
# =====================================================

print("12. Nested Dictionary")

employee = {
    "name": "Aamir",
    "address": {
        "city": "Ahmedabad",
        "state": "Gujarat"
    }
}

print(employee["address"]["city"])


# =====================================================
# 13. LOOP THROUGH LIST
# =====================================================

print("13. Loop Through List")

for student in students:
    print(student)


# =====================================================
# 14. LOOP THROUGH TUPLE
# =====================================================

print("14. Loop Through Tuple")

for color in colors:
    print(color)


# =====================================================
# 15. LOOP THROUGH SET
# =====================================================

print("15. Loop Through Set")

for number in numbers:
    print(number)


# =====================================================
# 16. LOOP THROUGH DICTIONARY
# =====================================================

print("16. Loop Through Dictionary")

for key in student:
    print(key, ":", student[key])


# =====================================================
# 17. UNPACKING LIST
# =====================================================

print("17. Unpacking List")

name1, name2, name3, name4 = students

print(name1)
print(name2)
print(name3)
print(name4)


# =====================================================
# 18. MEMBERSHIP OPERATOR
# =====================================================

print("18. Membership Operator")

print("Moin" in students)
print("Red" in colors)
print(50 in numbers)
print("name" in student)


# =====================================================
# 19. MUTABLE VS IMMUTABLE
# =====================================================

print("19. Mutable vs Immutable")

print("List -> Mutable")
print("Dictionary -> Mutable")
print("Set -> Mutable")

print("Tuple -> Immutable")


# =====================================================
# 20. COLLECTION COMPARISON
# =====================================================

print("20. Collection Comparison")

print("List -> Ordered, Mutable")
print("Tuple -> Ordered, Immutable")
print("Set -> Unordered, Unique")
print("Dictionary -> Key-Value Pair")


# =====================================================
# 21. REAL EXAMPLE
# =====================================================

print("21. Student List")

students = [
    "Moin",
    "Aamir",
    "Yasin",
    "Adil"
]

for student in students:
    print(student)


# =====================================================
# 22. REAL EXAMPLE
# =====================================================

print("22. Employee Details")

employee = {
    "id": 101,
    "name": "Aamir",
    "salary": 50000
}

print(employee)


# =====================================================
# 23. REAL EXAMPLE
# =====================================================

print("23. AI Model")

ai_model = {
    "model": "GPT-5",
    "temperature": 0.7,
    "max_tokens": 1000
}

print(ai_model)


# =====================================================
# 24. REAL EXAMPLE
# =====================================================

print("24. Subjects")

subjects = (
    "Python",
    "React",
    "AI",
    "ML"
)

for subject in subjects:
    print(subject)


# =====================================================
# 25. SUMMARY
# =====================================================

print("25. Summary")

# print("List")
# print("Tuple")
# print("Set")
# print("Dictionary")

# print("Indexing")
# print("Slicing")
# print("Looping")
# print("Nested Collections")
# print("Unpacking")
# print("Membership")
# print("Mutable vs Immutable")

# NOTE:
#
# Today we learned the four Python collections.
#
# ✔ List
# ✔ Tuple
# ✔ Set
# ✔ Dictionary
#
# We intentionally did NOT cover methods like:
#
# append()
# insert()
# remove()
# pop()
# clear()
# sort()
# reverse()
# update()
# keys()
# values()
# items()
#
# These belong to the next file:
#
# 📄 08_collection_methods.py
#
# This is exactly the same approach we followed in JavaScript:
#
# 07_array.js
# 08_array_methods.js