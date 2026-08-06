# =====================================================
# PYTHON EXCEPTION HANDLING
# =====================================================

print("=" * 50)
print("Python Exception Handling")
print("=" * 50)


# =====================================================
# 1. SIMPLE EXCEPTION
# =====================================================

print("1. Simple Exception")

try:

    number = 10 / 0

    print(number)

except:

    print("Something went wrong.")


# =====================================================
# 2. ZeroDivisionError
# =====================================================

print("2. ZeroDivisionError")

try:

    print(20 / 0)

except ZeroDivisionError:

    print("Cannot divide by zero.")


# =====================================================
# 3. ValueError
# =====================================================

print("3. ValueError")

try:

    age = int("Python")

except ValueError:

    print("Invalid Number")


# =====================================================
# 4. TypeError
# =====================================================

print("4. TypeError")

try:

    print(10 + "20")

except TypeError:

    print("Different data types.")


# =====================================================
# 5. IndexError
# =====================================================

print("5. IndexError")

try:

    students = ["Moin", "Aamir"]

    print(students[5])

except IndexError:

    print("Index not found.")


# =====================================================
# 6. KeyError
# =====================================================

print("6. KeyError")

try:

    student = {
        "name": "Moin"
    }

    print(student["marks"])

except KeyError:

    print("Key not available.")


# =====================================================
# 7. FileNotFoundError
# =====================================================

print("7. FileNotFoundError")

try:

    file = open("abc.txt")

except FileNotFoundError:

    print("File does not exist.")


# =====================================================
# 8. MULTIPLE EXCEPT
# =====================================================

print("8. Multiple Except")

try:

    number = int("Hello")

    print(20 / number)

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Division by zero")


# =====================================================
# 9. EXCEPTION AS e
# =====================================================

print("9. Exception as e")

try:

    print(20 / 0)

except Exception as error:

    print(error)


# =====================================================
# 10. ELSE
# =====================================================

print("10. Else")

try:

    print(20 / 2)

except:

    print("Error")

else:

    print("No Error")


# =====================================================
# 11. FINALLY
# =====================================================

print("11. Finally")

try:

    print("Database Connected")

finally:

    print("Database Closed")


# =====================================================
# 12. RAISE
# =====================================================

print("12. Raise")

age = 15

try:

    if age < 18:

        raise Exception("Age must be 18+")

except Exception as error:

    print(error)


# =====================================================
# 13. CUSTOM EXCEPTION
# =====================================================

print("13. Custom Exception")

class InvalidAge(Exception):

    pass

try:

    age = 15

    if age < 18:

        raise InvalidAge("Invalid Age")

except InvalidAge as error:

    print(error)


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Student Result")

try:

    marks = int(input("Enter Marks : "))

    print(marks)

except ValueError:

    print("Please enter numbers only.")


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. Employee Salary")

try:

    salary = float(input("Enter Salary : "))

    print(salary)

except ValueError:

    print("Invalid Salary")


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. Product")

try:

    stock = int(input("Enter Stock : "))

    print(stock)

except ValueError:

    print("Invalid Stock")


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. File Reader")

try:

    with open("students.txt") as file:

        print(file.read())

except FileNotFoundError:

    print("students.txt not found.")


# =====================================================
# 18. REAL EXAMPLE
# =====================================================

print("18. AI Prompt")

try:

    prompt = ""

    if prompt == "":

        raise Exception("Prompt cannot be empty.")

except Exception as error:

    print(error)


# =====================================================
# 19. SUMMARY
# =====================================================

print("19. Summary")

print("try")
print("except")
print("else")
print("finally")
print("raise")
print("Custom Exception")
print("Exception as e")
print("Multiple Except")


# NOTE:
#
# JavaScript
#
# try {
#
# }
# catch(error){
#
# }
# finally{
#
# }
#
#
# Python
#
# try:
#
# except:
#
# finally:
#
#
# JavaScript throw
#
# ↓
#
# Python raise
#
#
# Every production application
# uses Exception Handling.
#
# FastAPI
# Django
# Flask
# AI
# APIs
# Database
# File Handling
#
# all use try...except.