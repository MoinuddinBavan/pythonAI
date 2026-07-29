# =====================================================
# PYTHON FUNCTIONS
# =====================================================

print("=" * 50)
print("Python Functions")
print("=" * 50)


# =====================================================
# 1. CREATE A FUNCTION
# =====================================================

print("1. Create Function")

def welcome():
    print("Welcome to Python")

welcome()


# =====================================================
# 2. FUNCTION WITH PARAMETERS
# =====================================================

print("2. Function with Parameters")

def greet(name):
    print("Hello", name)

greet("Moin")
greet("Aamir")


# =====================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# =====================================================

print("3. Multiple Parameters")

def student(name, age):
    print("Name :", name)
    print("Age :", age)

student("Moin", 32)


# =====================================================
# 4. RETURN VALUE
# =====================================================

print("4. Return Value")

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# =====================================================
# 5. DEFAULT PARAMETERS
# =====================================================

print("5. Default Parameters")

def country(name, country="India"):
    print(name, "-", country)

country("Moin")
country("John", "USA")


# =====================================================
# 6. KEYWORD ARGUMENTS
# =====================================================

print("6. Keyword Arguments")

def employee(name, salary):
    print(name)
    print(salary)

employee(salary=50000, name="Aamir")


# =====================================================
# 7. POSITIONAL ARGUMENTS
# =====================================================

print("7. Positional Arguments")

employee("Yasin", 45000)


# =====================================================
# 8. ARBITRARY ARGUMENTS (*args)
# =====================================================

print("8. *args")

def total(*numbers):
    print(numbers)
    print(sum(numbers))

total(10, 20, 30)
total(5, 15, 25, 35)


# =====================================================
# 9. KEYWORD ARGUMENTS (**kwargs)
# =====================================================

print("9. **kwargs")

def profile(**data):
    print(data)

profile(name="Moin", city="Ahmedabad", age=32)


# =====================================================
# 10. LOCAL VARIABLE
# =====================================================

print("10. Local Variable")

def demo():
    message = "Hello"

    print(message)

demo()


# =====================================================
# 11. GLOBAL VARIABLE
# =====================================================

print("11. Global Variable")

company = "AIZ INFOTECHS"

def show_company():
    print(company)

show_company()


# =====================================================
# 12. RETURN MULTIPLE VALUES
# =====================================================

print("12. Multiple Return Values")

def calculation(a, b):
    return a + b, a - b

addition, subtraction = calculation(20, 10)

print(addition)
print(subtraction)


# =====================================================
# 13. FUNCTION CALLING FUNCTION
# =====================================================

print("13. Function Calling Function")

def hello():
    print("Hello")

def welcome():
    hello()
    print("Welcome")

welcome()


# =====================================================
# 14. RECURSION
# =====================================================

print("14. Recursion")

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)

countdown(5)


# =====================================================
# 15. DOCSTRING
# =====================================================

print("15. Docstring")

def square(number):
    """
    Returns square of a number.
    """

    return number * number

print(square(5))


# =====================================================
# 16. TYPE HINTS
# =====================================================

print("16. Type Hints")

def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(5, 4))


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. Student Result")

def result(name, marks):

    if marks >= 35:
        status = "Pass"
    else:
        status = "Fail"

    print(name, "-", status)

result("Moin", 80)
result("Aamir", 25)


# =====================================================
# 18. REAL EXAMPLE
# =====================================================

print("18. Employee Salary")

def salary_after_bonus(salary):

    bonus = salary * 0.10

    return salary + bonus

print(salary_after_bonus(50000))


# =====================================================
# 19. REAL EXAMPLE
# =====================================================

print("19. Product Discount")

def final_price(price, discount):

    return price - (price * discount / 100)

print(final_price(5000, 15))


# =====================================================
# 20. REAL EXAMPLE
# =====================================================

print("20. AI Prompt")

def generate_prompt(topic):

    return f"Explain {topic} in simple language."

print(generate_prompt("Machine Learning"))


# =====================================================
# 21. REAL EXAMPLE
# =====================================================

print("21. Login")

def login(username, password):

    if username == "admin" and password == "12345":
        return "Login Successful"

    return "Invalid Login"

print(login("admin", "12345"))


# =====================================================
# 22. SUMMARY
# =====================================================

print("22. Summary")

# print("def")
# print("Parameters")
# print("Arguments")
# print("return")
# print("Default Parameters")
# print("Keyword Arguments")
# print("*args")
# print("**kwargs")
# print("Local Variables")
# print("Global Variables")
# print("Recursion")
# print("Docstring")
# print("Type Hints")

# NOTE:
#
# JavaScript                Python
# -----------------------------------------
# function demo()      -> def demo():
# return               -> return
# parameters           -> parameters
# arguments            -> arguments
# ...args              -> *args
# object               -> **kwargs
#
# Functions are the foundation of:
# ✔ Flask
# ✔ Django
# ✔ FastAPI
# ✔ AI Projects
# ✔ Automation
# ✔ APIs