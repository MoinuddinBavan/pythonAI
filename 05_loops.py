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
# 2. PRINT MESSAGE MULTIPLE TIMES
# =====================================================

print("2. Print Message Multiple Times")

for i in range(1, 6):
    print(i, "Hello Moin")


# =====================================================
# 3. START LOOP FROM ZERO
# =====================================================

print("3. Start Loop From Zero")

for i in range(6):
    print(i)


# =====================================================
# 4. REVERSE LOOP
# =====================================================

print("4. Reverse Loop")

for i in range(10, 0, -1):
    print(i)


# =====================================================
# 5. EVEN NUMBERS
# =====================================================

print("5. Even Numbers")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# =====================================================
# 6. ODD NUMBERS
# =====================================================

print("6. Odd Numbers")

for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# =====================================================
# 7. MULTIPLICATION TABLE
# =====================================================

print("7. Multiplication Table")

table = 5

for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")


# =====================================================
# 8. SUM OF NUMBERS
# =====================================================

print("8. Sum of Numbers")

total = 0

for i in range(1, 11):
    total += i

print(total)


# =====================================================
# 9. WHILE LOOP
# =====================================================

print("9. While Loop")

number = 1

while number <= 5:
    print(number)
    number += 1


# =====================================================
# 10. BREAK
# =====================================================

print("10. Break")

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# =====================================================
# 11. CONTINUE
# =====================================================

print("11. Continue")

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# =====================================================
# 12. PASS
# =====================================================

print("12. Pass")

for i in range(1, 6):
    if i == 3:
        pass

    print(i)


# =====================================================
# 13. NESTED LOOP
# =====================================================

print("13. Nested Loop")

for row in range(1, 4):
    for col in range(1, 4):
        print("Row:", row, "Column:", col)


# =====================================================
# 14. STAR PATTERN
# =====================================================

print("14. Star Pattern")

for row in range(1, 6):
    stars = ""

    for col in range(row):
        stars += "*"

    print(stars)


# =====================================================
# 15. REVERSE STAR PATTERN
# =====================================================

print("15. Reverse Star Pattern")

for row in range(5, 0, -1):
    stars = ""

    for col in range(row):
        stars += "*"

    print(stars)


# =====================================================
# 16. RANGE()
# =====================================================

print("16. range()")

for i in range(5):
    print(i)

print("-----")

for i in range(2, 8):
    print(i)

print("-----")

for i in range(2, 20, 3):
    print(i)


# =====================================================
# 17. ENUMERATE()
# =====================================================

print("17. enumerate()")

students = ["Moin", "Aamir", "Yasin"]

for index, student in enumerate(students):
    print(index, student)


# =====================================================
# 18. FOR...ELSE
# =====================================================

print("18. for...else")

for i in range(1, 6):
    print(i)
else:
    print("Loop Finished")


# =====================================================
# 19. WHILE...ELSE
# =====================================================

print("19. while...else")

count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("While Loop Finished")


# =====================================================
# 20. REAL EXAMPLE
# =====================================================

print("20. Student Marks")

marks = [85, 74, 91, 63, 58]

for mark in marks:
    print(mark)


# =====================================================
# 21. REAL EXAMPLE
# =====================================================

print("21. Employee Salary")

salaries = [35000, 45000, 52000]

total = 0

for salary in salaries:
    total += salary

print("Total Salary =", total)


# =====================================================
# 22. REAL EXAMPLE
# =====================================================

print("22. Product List")

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

for product in products:
    print(product)


# =====================================================
# 23. REAL EXAMPLE
# =====================================================

print("23. AI Prompts")

prompts = [
    "Explain Python",
    "Write SQL Query",
    "Create React Component"
]

for prompt in prompts:
    print(prompt)


# =====================================================
# 24. SUMMARY
# =====================================================

print("24. Summary")

# print("for")
# print("while")
# print("break")
# print("continue")
# print("pass")
# print("nested loops")
# print("range()")
# print("enumerate()")
# print("for...else")
# print("while...else")

# NOTE:
# We already learned "for...of" in JavaScript.
#
# Python's "for" loop works similarly to JavaScript's "for...of".
#
# JavaScript
# for (let item of array)
#
# Python
# for item in array
#
# Python does NOT have a traditional "for...in" like JavaScript.
# In Python, "for ... in" is the normal loop syntax.