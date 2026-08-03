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
    print("You are eligible to vote.")


# =====================================================
# 2. if...else
# =====================================================

print("2. if...else")

marks = 28

if marks >= 35:
    print("Pass")
else:
    print("Fail")


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
        print("Please apply for a driving license.")
else:
    print("You are under age.")


# =====================================================
# 5. SHORT HAND if
# =====================================================

print("5. Short Hand if")

salary = 50000

if salary >= 40000: print("Bonus Approved")


# =====================================================
# 6. SHORT HAND if...else
# =====================================================

print("6. Short Hand if...else")

age = 17

print("Adult") if age >= 18 else print("Minor")


# =====================================================
# 7. LOGICAL OPERATOR - and
# =====================================================

print("7. Logical Operator - and")

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Login")


# =====================================================
# 8. LOGICAL OPERATOR - or
# =====================================================

print("8. Logical Operator - or")

is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted")
else:
    print("Access Denied")


# =====================================================
# 9. LOGICAL OPERATOR - not
# =====================================================

print("9. Logical Operator - not")

is_blocked = False

if not is_blocked:
    print("User Active")


# =====================================================
# 10. MEMBERSHIP OPERATOR
# =====================================================

print("10. Membership Operator")

students = ["Moin", "Aamir", "Yasin"]

if "Moin" in students:
    print("Student Found")


# =====================================================
# 11. IDENTITY OPERATOR
# =====================================================

print("11. Identity Operator")

a = [10, 20]
b = a

if a is b:
    print("Both variables refer to same object")


# =====================================================
# 12. MATCH CASE (Python 3.10+)
# =====================================================

print("12. Match Case")

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
# 13. REAL EXAMPLE
# =====================================================

print("13. Student Result")

marks = 91

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Employee Bonus")

salary = 55000

if salary >= 50000:
    print("Bonus Approved")
else:
    print("Bonus Not Approved")


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. Product Stock")

stock = 8

if stock > 0:
    print("Product Available")
else:
    print("Out of Stock")


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. Shopping Discount")

amount = 3500

if amount >= 3000:
    print("10% Discount")
else:
    print("No Discount")


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. AI Prompt")

temperature = 0.7

if temperature < 0.3:
    print("Focused Response")

elif temperature < 0.8:
    print("Balanced Response")

else:
    print("Creative Response")


# =====================================================
# 18. REAL EXAMPLE
# =====================================================

print("18. ATM Withdrawal")

balance = 12000
withdraw = 3000

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance :", balance)
else:
    print("Insufficient Balance")


# =====================================================
# 19. SUMMARY
# =====================================================

print("19. Summary")

# print("if")
# print("if...else")
# print("if...elif...else")
# print("Nested if")
# print("Short Hand if")
# print("Short Hand if...else")
# print("and")
# print("or")
# print("not")
# print("Membership Operator")
# print("Identity Operator")
# print("Match Case")
# print("Real-world Examples")