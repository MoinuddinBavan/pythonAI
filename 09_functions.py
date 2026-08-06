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
# 3. MULTIPLE PARAMETERS
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

result = add(20, 30)

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
# 6. POSITIONAL ARGUMENTS
# =====================================================

print("6. Positional Arguments")

def employee(name, salary):

    print(name)
    print(salary)

employee("Aamir", 50000)


# =====================================================
# 7. KEYWORD ARGUMENTS
# =====================================================

print("7. Keyword Arguments")

employee(salary=60000, name="Yasin")


# =====================================================
# 8. *args
# =====================================================

print("8. *args")

def total(*numbers):

    print(numbers)
    print(sum(numbers))

total(10, 20, 30)
total(5, 10, 15, 20)


# =====================================================
# 9. **kwargs
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

    message = "Python"

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

print("12. Return Multiple Values")

def calculate(a, b):

    return a+b, a-b, a*b

addition, subtraction, multiplication = calculate(20, 10)

print(addition)
print(subtraction)
print(multiplication)


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

# NOTE:
# Recursion belongs to a later topic.
# We are learning only the basic idea here.


# =====================================================
# 15. DOCSTRING
# =====================================================

print("15. Docstring")

def square(number):
    """
    Returns square of number.
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

# NOTE:
# Type Hints will be covered in detail later.


# =====================================================
# 17. LAMBDA FUNCTION
# =====================================================

print("17. Lambda Function")

square = lambda number: number * number

print(square(5))

# NOTE:
# Lambda belongs to the next topic.
# We are introducing it here only.


# =====================================================
# 18. REAL EXAMPLE
# =====================================================

print("18. Student Result")

def result(name, marks):

    if marks >= 35:
        status = "Pass"
    else:
        status = "Fail"

    print(name, "-", status)

result("Moin", 82)
result("Aamir", 28)


# =====================================================
# 19. REAL EXAMPLE
# =====================================================

print("19. Employee Salary")

def salary_after_bonus(salary):

    bonus = salary * 0.10

    return salary + bonus

print(salary_after_bonus(50000))


# =====================================================
# 20. REAL EXAMPLE
# =====================================================

print("20. Product Discount")

def final_price(price, discount):

    return price - (price * discount / 100)

print(final_price(2500, 15))


# =====================================================
# 21. REAL EXAMPLE
# =====================================================

print("21. AI Prompt")

def ai_prompt(topic):

    return f"Explain {topic} in simple language."

print(ai_prompt("Machine Learning"))


# =====================================================
# 22. REAL EXAMPLE
# =====================================================

print("22. Login")

def login(username, password):

    if username == "admin" and password == "12345":
        return "Login Successful"

    return "Invalid Login"

print(login("admin", "12345"))


# =====================================================
# 23. SUMMARY
# =====================================================

print("23. Summary")

print("def")
print("Parameters")
print("Arguments")
print("Return")
print("Default Parameters")
print("Positional Arguments")
print("Keyword Arguments")
print("*args")
print("**kwargs")
print("Local Variable")
print("Global Variable")
print("Recursion")
print("Docstring")
print("Type Hints")
print("Lambda")


# =====================================================
# PYTHON LAMBDA FUNCTIONS
# =====================================================

print("=" * 50)
print("Python Lambda Functions")
print("=" * 50)


# =====================================================
# 1. SIMPLE LAMBDA
# =====================================================

print("1. Simple Lambda")

square = lambda number: number * number

print(square(5))


# =====================================================
# 2. LAMBDA WITH TWO PARAMETERS
# =====================================================

print("2. Two Parameters")

add = lambda a, b: a + b

print(add(10, 20))


# =====================================================
# 3. LAMBDA WITH THREE PARAMETERS
# =====================================================

print("3. Three Parameters")

total = lambda a, b, c: a + b + c

print(total(10, 20, 30))


# =====================================================
# 4. NORMAL FUNCTION VS LAMBDA
# =====================================================

print("4. Normal Function vs Lambda")

def square1(number):
    return number * number

square2 = lambda number: number * number

print(square1(5))
print(square2(5))


# =====================================================
# 5. LAMBDA INSIDE VARIABLE
# =====================================================

print("5. Lambda Variable")

multiply = lambda a, b: a * b

print(multiply(8, 6))


# =====================================================
# 6. LAMBDA WITH if...else
# =====================================================

print("6. Lambda with if...else")

result = lambda marks: "Pass" if marks >= 35 else "Fail"

print(result(80))
print(result(22))


# =====================================================
# 7. sorted()
# =====================================================

numbers = [45, 12, 78, 25, 90]

print(sorted(numbers))
print(sorted(numbers, reverse=True))



# =====================================================
# 8. sorted() with Lambda
# =====================================================

students = [
    ("Moin", 82),
    ("Aamir", 65),
    ("Yasin", 91)
]

print(sorted(students, key=lambda student: student[1]))


# =====================================================
# 9. map()
# =====================================================

print("9. map()")

numbers = [1, 2, 3, 4, 5]

square = list(map(lambda x: x * x, numbers))

print(square)


# =====================================================
# 10. filter()
# =====================================================

print("10. filter()")

numbers = [10, 15, 20, 25, 30]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


# =====================================================
# 11. reduce()
# =====================================================

print("11. reduce()")

from functools import reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numbers)

print(total)


# =====================================================
# 12. max()
# =====================================================

print("12. max()")

students = [
    ("Moin", 82),
    ("Aamir", 65),
    ("Yasin", 91)
]

highest = max(students, key=lambda student: student[1])

print(highest)


# =====================================================
# 13. min()
# =====================================================

print("13. min()")

lowest = min(students, key=lambda student: student[1])

print(lowest)


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Student Result")

marks = [85, 72, 91, 64]

result = list(map(lambda x: "Pass" if x >= 35 else "Fail", marks))

print(result)


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. Employee Bonus")

salary = [30000, 45000, 60000]

bonus = list(map(lambda x: x + 5000, salary))

print(bonus)


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. Product Discount")

prices = [1200, 2500, 4000]

discount = list(map(lambda x: x * 0.90, prices))

print(discount)


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. AI Temperature")

temperatures = [0.2, 0.7, 1.0]

labels = list(map(
    lambda t: "Focused" if t < 0.3 else
              "Balanced" if t < 0.8 else
              "Creative",
    temperatures
))

print(labels)


# =====================================================
# 18. SUMMARY
# =====================================================

print("18. Summary")

print("lambda")
print("Multiple Parameters")
print("if...else")
print("sorted()")
print("sort()")
print("map()")
print("filter()")
print("reduce()")
print("max()")
print("min()")





# =====================================================
# PYTHON SCOPE & RECURSION
# =====================================================

print("=" * 50)
print("Python Scope & Recursion")
print("=" * 50)


# =====================================================
# 1. LOCAL VARIABLE
# =====================================================

print("1. Local Variable")

def student():

    name = "Moin"

    print(name)

student()

# print(name)   # Error


# =====================================================
# 2. GLOBAL VARIABLE
# =====================================================

print("2. Global Variable")

company = "AIZ INFOTECHS"

def office():

    print(company)

office()

print(company)


# =====================================================
# 3. LOCAL VS GLOBAL
# =====================================================

print("3. Local vs Global")

name = "Global"

def demo():

    name = "Local"

    print(name)

demo()

print(name)


# =====================================================
# 4. global KEYWORD
# =====================================================

print("4. global Keyword")

count = 10

def update():

    global count

    count += 5

update()

print(count)


# =====================================================
# 5. GLOBAL VARIABLE INSIDE FUNCTION
# =====================================================

print("5. Global Variable")

message = "Welcome"

def show():

    print(message)

show()


# =====================================================
# 6. NESTED FUNCTION
# =====================================================

print("6. Nested Function")

def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()

outer()


# =====================================================
# 7. RECURSION
# =====================================================

print("7. Recursion")

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)

countdown(5)


# =====================================================
# 8. FACTORIAL USING RECURSION
# =====================================================

print("8. Factorial")

def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))


# =====================================================
# 9. SUM USING RECURSION
# =====================================================

print("9. Sum Using Recursion")

def total(number):

    if number == 0:
        return 0

    return number + total(number - 1)

print(total(5))


# =====================================================
# 10. FIBONACCI
# =====================================================

print("10. Fibonacci")

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(10):

    print(fibonacci(i))


# =====================================================
# 11. RECURSION VS LOOP
# =====================================================

print("11. Recursion vs Loop")

print("Loop")

for i in range(1, 6):

    print(i)

print("Recursion")

def display(number):

    if number == 6:
        return

    print(number)

    display(number + 1)

display(1)


# =====================================================
# 12. REAL EXAMPLE
# =====================================================

print("12. Student")

student_name = "Moin"

def student():

    marks = 85

    print(student_name)

    print(marks)

student()


# =====================================================
# 13. REAL EXAMPLE
# =====================================================

print("13. Employee")

company = "AIZ INFOTECHS"

def employee():

    salary = 50000

    print(company)

    print(salary)

employee()


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Shopping")

cart = [1200, 800, 600]

def bill():

    total = sum(cart)

    print(total)

bill()


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. AI Prompt")

prompt = "Explain Machine Learning"

def ai():

    print(prompt)

ai()


# =====================================================
# 16. SUMMARY
# =====================================================

print("16. Summary")

print("Local Variable")
print("Global Variable")
print("global Keyword")
print("Nested Function")
print("Recursion")
print("Factorial")
print("Sum")
print("Fibonacci")
print("Recursion vs Loop")