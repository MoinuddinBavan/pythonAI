# =====================================================
# PYTHON LOOPS
# =====================================================

print("=" * 50)
print("Python Loops")
print("=" * 50)


# =====================================================
# 1. FOR LOOP
# =====================================================

print("1. For Loop")

for i in range(1, 6):
    print(i)


# =====================================================
# 2. WHILE LOOP
# =====================================================

print("2. While Loop")

number = 1

while number <= 5:
    print(number)
    number += 1


# =====================================================
# 3. RANGE()
# =====================================================

print("3. range()")

print(range(5))

for i in range(5):
    print(i)

print("----------")

for i in range(2, 7):
    print(i)

print("----------")

for i in range(2, 11, 2):
    print(i)


# =====================================================
# 4. BREAK
# =====================================================

print("4. break")

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# =====================================================
# 5. CONTINUE
# =====================================================

print("5. continue")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)


# =====================================================
# 6. PASS
# =====================================================

print("6. pass")

for i in range(1, 6):

    if i == 3:
        pass

    print(i)


# =====================================================
# 7. REVERSE LOOP
# =====================================================

print("7. Reverse Loop")

for i in range(10, 0, -1):
    print(i)


# =====================================================
# 8. EVEN NUMBERS
# =====================================================

print("8. Even Numbers")

for i in range(1, 21):

    if i % 2 == 0:
        print(i)


# =====================================================
# 9. ODD NUMBERS
# =====================================================

print("9. Odd Numbers")

for i in range(1, 21):

    if i % 2 != 0:
        print(i)


# =====================================================
# 10. MULTIPLICATION TABLE
# =====================================================

print("10. Multiplication Table")

table = 7

for i in range(1, 11):

    print(f"{table} x {i} = {table * i}")


# =====================================================
# 11. SUM OF NUMBERS
# =====================================================

print("11. Sum of Numbers")

total = 0

for i in range(1, 101):
    total += i

print(total)


# =====================================================
# 12. NESTED LOOP
# =====================================================

print("12. Nested Loop")

for row in range(1, 4):

    for col in range(1, 4):

        print("Row:", row, "Column:", col)


# =====================================================
# 13. STAR PATTERN
# =====================================================

print("13. Star Pattern")

for row in range(1, 6):

    stars = ""

    for col in range(row):

        stars += "*"

    print(stars)


# =====================================================
# 14. REVERSE STAR PATTERN
# =====================================================

print("14. Reverse Star Pattern")

for row in range(5, 0, -1):

    stars = ""

    for col in range(row):

        stars += "*"

    print(stars)


# =====================================================
# 15. LOOP THROUGH LIST
# =====================================================

print("15. Loop Through List")

students = [
    "Moin",
    "Aamir",
    "Yasin"
]

for student in students:
    print(student)


# =====================================================
# 16. LOOP THROUGH TUPLE
# =====================================================

print("16. Loop Through Tuple")

colors = (
    "Red",
    "Green",
    "Blue"
)

for color in colors:
    print(color)


# =====================================================
# 17. LOOP THROUGH SET
# =====================================================

print("17. Loop Through Set")

numbers = {
    10,
    20,
    30,
    40
}

for number in numbers:
    print(number)


# =====================================================
# 18. LOOP THROUGH DICTIONARY
# =====================================================

print("18. Loop Through Dictionary")

employee = {
    "name": "Moin",
    "age": 32,
    "city": "Ahmedabad"
}

for key in employee:

    print(key, ":", employee[key])


# =====================================================
# 19. ENUMERATE()
# =====================================================

print("19. enumerate()")

students = [
    "Moin",
    "Aamir",
    "Yasin"
]

for index, student in enumerate(students):

    print(index, student)


# =====================================================
# 20. ZIP()
# =====================================================

print("20. zip()")

names = [
    "Moin",
    "Aamir",
    "Yasin"
]

marks = [
    85,
    72,
    91
]

for name, mark in zip(names, marks):

    print(name, mark)


# =====================================================
# 21. FOR...ELSE
# =====================================================

print("21. for...else")

for i in range(1, 6):
    print(i)

else:
    print("Loop Finished")


# =====================================================
# 22. WHILE...ELSE
# =====================================================

print("22. while...else")

count = 1

while count <= 5:

    print(count)

    count += 1

else:
    print("While Loop Finished")


# =====================================================
# 23. REAL EXAMPLE
# =====================================================

print("23. Student Marks")

marks = [
    85,
    74,
    91,
    63,
    58
]

for mark in marks:

    print(mark)


# =====================================================
# 24. REAL EXAMPLE
# =====================================================

print("24. Employee Salary")

salaries = [
    35000,
    45000,
    52000
]

total_salary = 0

for salary in salaries:

    total_salary += salary

print("Total Salary :", total_salary)


# =====================================================
# 25. REAL EXAMPLE
# =====================================================

print("25. Product List")

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

for product in products:

    print(product)


# =====================================================
# 26. REAL EXAMPLE
# =====================================================

print("26. Shopping Cart")

cart = [
    250,
    180,
    420,
    150
]

bill = 0

for item in cart:

    bill += item

print("Total Bill :", bill)


# =====================================================
# 27. REAL EXAMPLE
# =====================================================

print("27. AI Prompts")

prompts = [
    "Explain Python",
    "Create SQL Query",
    "Write React Component"
]

for prompt in prompts:

    print(prompt)


# =====================================================
# 28. REAL EXAMPLE
# =====================================================

print("28. API Data")

users = [
    {"name": "Moin"},
    {"name": "Aamir"},
    {"name": "Yasin"}
]

for user in users:

    print(user["name"])


# =====================================================
# 29. SUMMARY
# =====================================================

print("29. Summary")

# print("for")
# print("while")
# print("range()")
# print("break")
# print("continue")
# print("pass")
# print("Nested Loop")
# print("Loop Through List")
# print("Loop Through Tuple")
# print("Loop Through Set")
# print("Loop Through Dictionary")
# print("enumerate()")
# print("zip()")
# print("for...else")
# print("while...else")