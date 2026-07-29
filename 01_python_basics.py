# =====================================================
# PYTHON BASICS
# =====================================================

print("=" * 50)
print("Python Basics")
print("=" * 50)


# =====================================================
# 1. HELLO WORLD
# =====================================================

print("1. Hello World")

print("Hello Moin")


# =====================================================
# 2. COMMENTS
# =====================================================

print("2. Comments")

# Single line comment

"""
Multi-line comment

Useful for documentation.

"""


# =====================================================
# 3. PRINT MULTIPLE VALUES
# =====================================================

print("3. Print Multiple Values")

name = "Moin"
age = 32

print(name, age)


# =====================================================
# 4. VARIABLES
# =====================================================

print("4. Variables")

company = "AIZ INFOTECHS"
salary = 50000
is_developer = True

print(company)
print(salary)
print(is_developer)


# =====================================================
# 5. MULTIPLE VARIABLE ASSIGNMENT
# =====================================================

print("5. Multiple Variables")

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)


# =====================================================
# 6. SAME VALUE
# =====================================================

print("6. Same Value")

a = b = c = 100

print(a)
print(b)
print(c)


# =====================================================
# 7. VARIABLE SWAPPING
# =====================================================

print("7. Variable Swapping")

first = 10
second = 20

print(first, second)

first, second = second, first

print(first, second)


# =====================================================
# 8. VARIABLE TYPES
# =====================================================

print("8. Variable Types")

name = "Moin"
age = 32
height = 5.8
is_married = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_married))


# =====================================================
# 9. USER INPUT
# =====================================================

print("9. User Input")

student = input("Enter Student Name : ")
student_age = int(input("Enter your Age : "))

print("Welcome", student)
print("You are", student_age, "years old")


# =====================================================
# 10. INTEGER INPUT
# =====================================================

print("10. Integer Input")

marks = int(input("Enter Marks : "))

print("Marks :", marks)


# =====================================================
# 11. FLOAT INPUT
# =====================================================

print("11. Float Input")

price = float(input("Enter Price : "))

print(price)


# =====================================================
# 12. F-STRING
# =====================================================

print("12. F String")

name = "Moin"
course = "Python"

print(f"{name} is learnign {course} programming.")



# =====================================================
# 13. FORMAT()
# =====================================================

print("13. format()")

print("{} earns ₹{}".format("Aamir", 50000))


# =====================================================
# 14. STRING MULTIPLICATION
# =====================================================

print("14. String Multiplication")

print("*" * 3)


# =====================================================
# 15. ESCAPE CHARACTERS
# =====================================================

print("15. Escape Characters")

# \n = New Line
print("Hello\nWorld")

# \t = Tab Space
print("Python\tProgramming")

# \' = Single Quote
print('It\'s Python')

# \" = Double Quote
print("He said \"Hello\"")

# \\ = Backslash
print("C:\\Users\\Moin")

# \r = Carriage Return
print("Hello\rHi")

# \b = Backspace
print("Helloo\b")

# \n\t = New Line + Tab
print("Name:\n\tMoin")


# =====================================================
# 16. KEYWORDS
# =====================================================

print("16. Keywords")

import keyword

print(keyword.kwlist)

# keyword          → Built-in Python module
# keyword.kwlist   → Shows all Python keywords
# keyword.iskeyword() → Checks whether a word is a keyword

# =====================================================
# 17. VARIABLE NAMING
# =====================================================

print("17. Variable Naming")

student_name = "Moin"

StudentName = "Aamir"

studentName = "Yasin"

print(student_name)
print(StudentName)
print(studentName)


# ✅ Right Way
# firstname
# first_name
# _firstname
# firstName
# FirstName
# firstname99


# ❌ Wrong Way
# first name
# first-name
# 9firstname
# first@name
# first#name
# first$name
# class
# if
# for
# while
# True
# False
# None

# =====================================================
# 18. CONSTANT
# =====================================================

print("18. Constant")

PI = 3.14159

print(PI)

# Python doesn't have real constants.
# We use uppercase by convention.


# =====================================================
# 19. MEMORY ADDRESS
# =====================================================

print("19. Memory Address")

number = 100

print(id(number))


# =====================================================
# 20. DELETE VARIABLE
# =====================================================

print("20. Delete Variable")

temp = "Temporary"

print(temp)

del temp

# print(temp)


# =====================================================
# PRACTICE ASSIGNMENTS
# =====================================================

print("Practice Assignments")

# Assignment 1:
# Print your name, age and city.

# Assignment 2:
# Take your company name from input.

# Assignment 3:
# Take two numbers and print their sum.

# Assignment 4:
# Swap two variables.

# Assignment 5:
# Print variable data types.

# Assignment 6:
# Print using f-string.

# Assignment 7:
# Print using format().

# Assignment 8:
# Print 50 stars using string multiplication.

# Assignment 9:
# Print all Python keywords.

# Assignment 10:
# Print memory address using id().



# 1. Why is Python called an interpreted language?

# 2. What is a variable?

# 3. What is dynamic typing?

# 4. Difference between int and float?

# 5. What does type() do?

# 6. Difference between input() and print()?

# 7. What is f-string?

# 8. Difference between format() and f-string?

# 9. What is id()?

# 10. Does Python have constants?