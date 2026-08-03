# =====================================================
# PYTHON OPERATORS
# =====================================================

# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators (Basic)
# 8. Operator Precedence
# 9. Real-World Examples
# 10. Practice Assignments
# 11. Interview Questions


# =====================================================
# PYTHON OPERATORS
# =====================================================

print("=" * 50)
print("Python Operators")
print("=" * 50)


# =====================================================
# 1. ARITHMETIC OPERATORS
# =====================================================

print("1. Arithmetic Operators")

a = 20
b = 6

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Power :", a ** b)


# =====================================================
# 2. ADDITION (+)
# =====================================================

print("2. Addition")

num1 = 100
num2 = 50

print(num1 + num2)


# =====================================================
# 3. SUBTRACTION (-)
# =====================================================

print("3. Subtraction")

print(num1 - num2)


# =====================================================
# 4. MULTIPLICATION (*)
# =====================================================

print("4. Multiplication")

print(num1 * num2)


# =====================================================
# 5. DIVISION (/)
# =====================================================

print("5. Division")

print(num1 / num2)

# Division always returns float.


# =====================================================
# 6. FLOOR DIVISION (//)
# =====================================================

print("6. Floor Division")

print(25 // 4)
print(20 // 3)

# Returns only the integer part.


# =====================================================
# 7. MODULUS (%)
# =====================================================

print("7. Modulus")

print(25 % 4)
print(20 % 3)

# Returns the remainder.


# =====================================================
# 8. EXPONENT (**)
# =====================================================

print("8. Exponent")

print(5 ** 2)
print(2 ** 5)

# Power calculation.


# =====================================================
# 9. ASSIGNMENT OPERATOR (=)
# =====================================================

print("9. Assignment Operator")

salary = 50000

print(salary)


# =====================================================
# 10. ADD AND ASSIGN (+=)
# =====================================================

print("10. +=")

salary = 50000

salary += 5000

print(salary)


# =====================================================
# 11. SUBTRACT AND ASSIGN (-=)
# =====================================================

print("11. -=")

salary -= 2000

print(salary)


# =====================================================
# 12. MULTIPLY AND ASSIGN (*=)
# =====================================================

print("12. *=")

bonus = 5

bonus *= 2

print(bonus)


# =====================================================
# 13. DIVIDE AND ASSIGN (/=)
# =====================================================

print("13. /=")

amount = 100

amount /= 4

print(amount)


# =====================================================
# 14. FLOOR DIVIDE AND ASSIGN (//=)
# =====================================================

print("14. //=")

number = 25

number //= 4

print(number)


# =====================================================
# 15. MODULUS AND ASSIGN (%=)
# =====================================================

print("15. %=")

number = 25

number %= 4

print(number)


# =====================================================
# 16. POWER AND ASSIGN (**=)
# =====================================================

print("16. **=")

number = 5

number **= 2

print(number)


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. Employee Salary")

salary = 45000
bonus = 5000

total_salary = salary + bonus

print("Salary :", salary)
print("Bonus :", bonus)
print("Total :", total_salary)


# =====================================================
# 18. REAL EXAMPLE
# =====================================================

print("18. Shopping Bill")

mobile = 25000
cover = 500
charger = 1200

bill = mobile + cover + charger

print("Total Bill :", bill)


# =====================================================
# 19. REAL EXAMPLE
# =====================================================

print("19. Student Percentage")

total_marks = 500
obtained_marks = 420

percentage = (obtained_marks / total_marks) * 100

print("Percentage :", percentage)


# =====================================================
# 20. REAL EXAMPLE
# =====================================================

print("20. Area of Rectangle")

length = 15
width = 8

area = length * width

print("Area :", area)


# =====================================================
# 21. SUMMARY
# =====================================================

print("21. Summary")

# print("+  Addition")
# print("-  Subtraction")
# print("*  Multiplication")
# print("/  Division")
# print("// Floor Division")
# print("%  Modulus")
# print("** Exponent")

# print("=")
# print("+=")
# print("-=")
# print("*=")
# print("/=")
# print("//=")
# print("%=")
# print("**=")

# =====================================================
# 22. COMPARISON OPERATORS
# =====================================================

print("22. Comparison Operators")

a = 20
b = 10

print("a =", a)
print("b =", b)

print("Equal (==) :", a == b)
print("Not Equal (!=) :", a != b)
print("Greater Than (>) :", a > b)
print("Less Than (<) :", a < b)
print("Greater Than or Equal (>=) :", a >= b)
print("Less Than or Equal (<=) :", a <= b)


# =====================================================
# 23. EQUAL TO (==)
# =====================================================

print("23. Equal To (==)")

username = "moin"

print(username == "moin")
print(username == "admin")



# =====================================================
# 24. NOT EQUAL TO (!=)
# =====================================================

print("24. Not Equal To (!=)")

age = 18

print(age != 18)
print(age != 21)


# =====================================================
# 25. GREATER THAN (>)
# =====================================================

print("25. Greater Than (>)")

marks = 85

print(marks > 35)
print(marks > 90)


# =====================================================
# 26. LESS THAN (<)
# =====================================================

print("26. Less Than (<)")

temperature = 25

print(temperature < 30)
print(temperature < 20)


# =====================================================
# 27. GREATER THAN OR EQUAL (>=)
# =====================================================

print("27. Greater Than Or Equal (>=)")

salary = 50000

print(salary >= 50000)
print(salary >= 60000)


# =====================================================
# 28. LESS THAN OR EQUAL (<=)
# =====================================================

print("28. Less Than Or Equal (<=)")

stock = 5

print(stock <= 10)
print(stock <= 2)


# =====================================================
# 29. LOGICAL OPERATORS
# =====================================================

print("29. Logical Operators")

age = 25
citizen = True

print(age >= 18 and citizen)
print(age >= 18 or citizen)
print(not citizen)


# =====================================================
# 30. AND OPERATOR
# =====================================================

print("30. AND Operator")

username = "admin"
password = "1234"

print(username == "admin" and password == "1234")
print(username == "admin" and password == "0000")


# =====================================================
# 31. OR OPERATOR
# =====================================================

print("31. OR Operator")

is_admin = False
is_manager = True

print(is_admin or is_manager)

is_admin = False
is_manager = False

print(is_admin or is_manager)


# =====================================================
# 32. NOT OPERATOR
# =====================================================

print("32. NOT Operator")

is_logged_in = True

print(not is_logged_in)

is_logged_in = False

print(not is_logged_in)


# =====================================================
# 33. IDENTITY OPERATORS
# =====================================================

print("33. Identity Operators")

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)

print(x is not z)


# =====================================================
# 34. MEMBERSHIP OPERATORS
# =====================================================

print("34. Membership Operators")

students = ["Moin", "Aamir", "Yasin"]

print("Moin" in students)
print("Akib" in students)

print("Akib" not in students)
print("Yasin" not in students)


# =====================================================
# 35. REAL EXAMPLE
# =====================================================

print("35. Student Result")

marks = 72

print("Passed :", marks >= 35)


# =====================================================
# 36. REAL EXAMPLE
# =====================================================

print("36. Voting Eligibility")

age = 19

print("Eligible :", age >= 18)


# =====================================================
# 37. REAL EXAMPLE
# =====================================================

print("37. Login System")

username = "admin"
password = "12345"

login = username == "admin" and password == "12345"

print(login)


# =====================================================
# 38. REAL EXAMPLE
# =====================================================

print("38. Product Search")

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

print("Laptop" in products)
print("Mobile" in products)


# =====================================================
# 39. SUMMARY
# =====================================================

# print("39. Summary")

# print("==  Equal")
# print("!=  Not Equal")
# print(">   Greater Than")
# print("<   Less Than")
# print(">=  Greater Than or Equal")
# print("<=  Less Than or Equal")

# print("and")
# print("or")
# print("not")

# print("is")
# print("is not")

# print("in")
# print("not in")



# NOTE:
# We have covered:
# ✔ Arithmetic Operators
# ✔ Assignment Operators
# ✔ Comparison Operators
# ✔ Logical Operators
# ✔ Identity Operators
# ✔ Membership Operators
#
# Bitwise Operators are rarely used in day-to-day web development
# or AI projects. We'll learn the basics next for interview purposes.



# =====================================================
# 40. BITWISE OPERATORS
# =====================================================

print("40. Bitwise Operators")

a = 10      # 1010
b = 4       # 0100

print("a =", a)
print("b =", b)

print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

# We will not go deep into Bitwise Operators because
# they are rarely used in Web Development and AI.
# Basic knowledge is enough for interviews.


# =====================================================
# 41. BITWISE AND (&)
# =====================================================

print("41. Bitwise AND")

print(10 & 4)


# =====================================================
# 42. BITWISE OR (|)
# =====================================================

print("42. Bitwise OR")

print(10 | 4)


# =====================================================
# 43. BITWISE XOR (^)
# =====================================================

print("43. Bitwise XOR")

print(10 ^ 4)


# =====================================================
# 44. BITWISE NOT (~)
# =====================================================

print("44. Bitwise NOT")

print(~10)


# =====================================================
# 45. LEFT SHIFT (<<)
# =====================================================

print("45. Left Shift")

print(10 << 1)
print(10 << 2)


# =====================================================
# 46. RIGHT SHIFT (>>)
# =====================================================

print("46. Right Shift")

print(10 >> 1)
print(10 >> 2)


# =====================================================
# 47. OPERATOR PRECEDENCE
# =====================================================

print("47. Operator Precedence")

result = 10 + 5 * 2

print(result)

result = (10 + 5) * 2

print(result)

# Parentheses have the highest priority.


# =====================================================
# 48. REAL EXAMPLE
# =====================================================

print("48. Employee Bonus")

salary = 50000
bonus = 5000

total = salary + bonus

print("Total Salary :", total)


# =====================================================
# 49. REAL EXAMPLE
# =====================================================

print("49. Shopping Discount")

price = 2500
discount = 10

final_price = price - (price * discount / 100)

print("Final Price :", final_price)


# =====================================================
# 50. REAL EXAMPLE
# =====================================================

print("50. Student Result")

marks = 82

passed = marks >= 35

print("Passed :", passed)


# =====================================================
# 51. REAL EXAMPLE
# =====================================================

print("51. Age Verification")

age = 21

eligible = age >= 18

print("Eligible :", eligible)


# =====================================================
# 52. REAL EXAMPLE
# =====================================================

print("52. Login Verification")

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Login")


# =====================================================
# 53. REAL EXAMPLE
# =====================================================

print("53. Product Search")

products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor"
]

search = "Laptop"

print(search in products)


# =====================================================
# 54. REAL EXAMPLE
# =====================================================

print("54. AI API Configuration")

temperature = 0.7
max_tokens = 1000

print(temperature > 0)
print(max_tokens >= 500)


# =====================================================
# 55. SUMMARY
# =====================================================

print("55. Summary")

# print("Arithmetic Operators")
# print("Assignment Operators")
# print("Comparison Operators")
# print("Logical Operators")
# print("Identity Operators")
# print("Membership Operators")
# print("Bitwise Operators")
# print("Operator Precedence")
# print("Real-world Examples")