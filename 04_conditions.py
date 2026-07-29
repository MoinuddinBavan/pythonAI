# =====================================================
# PYTHON CONDITIONS
# =====================================================

print("=" * 50)
print("Python Conditions")
print("=" * 50)


# =====================================================
# 1. SIMPLE if
# =====================================================

print("1. Simple if")

age = 20

if age >= 18:
    print("You can vote.")


# =====================================================
# 2. if...else
# =====================================================

print("2. if...else")

age = 16

if age >= 18:
    print("Eligible for voting")
else:
    print("Not Eligible")


# =====================================================
# 3. if...elif...else
# =====================================================

print("3. if...elif...else")

marks = 82

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

elif marks >= 35:
    print("Grade C")

else:
    print("Fail")


# =====================================================
# 4. NESTED if
# =====================================================

print("4. Nested if")

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("Apply for a driving license.")
else:
    print("You are underage.")


# =====================================================
# 5. COMPARISON OPERATORS
# =====================================================

print("5. Comparison Operators")

a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# =====================================================
# 6. LOGICAL OPERATORS
# =====================================================

print("6. Logical Operators")

age = 25
salary = 40000

print(age >= 18 and salary >= 30000)
print(age >= 18 or salary >= 50000)
print(not(age >= 18))


# =====================================================
# 7. MEMBERSHIP OPERATOR
# =====================================================

print("7. Membership Operator")

students = ["Moin", "Aamir", "Yasin"]

if "Moin" in students:
    print("Student Found")


# =====================================================
# 8. IDENTITY OPERATOR
# =====================================================

print("8. Identity Operator")

x = [1, 2]
y = x

print(x is y)
print(x is not y)


# =====================================================
# 9. TERNARY OPERATOR
# =====================================================

print("9. Ternary Operator")

age = 22

message = "Adult" if age >= 18 else "Minor"

print(message)


# =====================================================
# 10. MATCH CASE (Python 3.10+)
# =====================================================

print("10. Match Case")

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend")


# =====================================================
# 11. REAL EXAMPLE
# =====================================================

print("11. Student Result")

marks = 58

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# =====================================================
# 12. REAL EXAMPLE
# =====================================================

print("12. Login System")

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Username or Password")


# =====================================================
# 13. REAL EXAMPLE
# =====================================================

print("13. ATM Withdrawal")

balance = 5000
withdraw = 3000

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Employee Bonus")

salary = 60000

if salary >= 50000:
    print("Bonus Approved")
else:
    print("Bonus Not Approved")


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. Product Stock")

stock = 12

if stock > 0:
    print("Product Available")
else:
    print("Out of Stock")


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. AI Model Settings")

temperature = 0.7

if temperature < 0.3:
    print("Focused Responses")

elif temperature < 0.8:
    print("Balanced Responses")

else:
    print("Creative Responses")


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. Age Category")

age = 65

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")


# =====================================================
# 18. SUMMARY
# =====================================================

print("18. Summary")

# print("if")
# print("if...else")
# print("if...elif...else")
# print("Nested if")
# print("Comparison Operators")
# print("Logical Operators")
# print("Membership Operator")
# print("Identity Operator")
# print("Ternary Operator")
# print("Match Case")
# print("Real-world Examples")