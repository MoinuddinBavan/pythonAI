# =====================================================
# PYTHON DECORATORS
# =====================================================

print("=" * 50)
print("Python Decorators")
print("=" * 50)


# =====================================================
# 1. FUNCTION STORED IN VARIABLE
# =====================================================

print("1. Function Stored in Variable")


def greet():
    return "Hello"


message = greet

print(message())


greet() # Calling the function directly.
greet # Referring to the function without calling it.
greet.__name__ # Getting the name of the function.

# Function can be stored in a variable.


# =====================================================
# 2. FUNCTION AS ARGUMENT
# =====================================================

print("2. Function as Argument")


def greet():
    return "Hello"

def execute(function):
    print(function())


execute(greet)


# A function can be passed to another function.


# =====================================================
# 3. FUNCTION INSIDE FUNCTION
# =====================================================

print("3. Function Inside Function")


def outer():

    def inner():
        print("Inner Function")

    inner()


outer()


# =====================================================
# 4. RETURN FUNCTION FROM FUNCTION
# =====================================================

print("4. Return Function")


def outer():

    def inner():
        print("Hello from Inner")

    return inner


result = outer()

result()


# =====================================================
# 5. BASIC DECORATOR
# =====================================================

print("5. Basic Decorator")


def my_decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


def greet():

    print("Hello Moin")


greet = my_decorator(greet)

greet()


# =====================================================
# 6. @ DECORATOR SYNTAX
# =====================================================

print("6. @ Decorator Syntax")


def my_decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


@my_decorator
def welcome():

    print("Welcome to Python")


welcome()


# @my_decorator is equivalent to:
#
# welcome = my_decorator(welcome)


# =====================================================
# 7. UNDERSTAND WRAPPER
# =====================================================

print("7. Wrapper")


def decorator(function):

    def wrapper():

        print("Start")

        function()

        print("End")

    return wrapper


@decorator
def task():

    print("Task Running")


task()


# FLOW:
#
# task()
#    ↓
# wrapper()
#    ↓
# Start
#    ↓
# Original task()
#    ↓
# End


# =====================================================
# 8. DECORATOR WITH ARGUMENTS
# =====================================================

print("8. Decorator with Arguments")


def decorator(function):

    def wrapper(name):

        print("Before")

        function(name)

        print("After")

    return wrapper


@decorator
def greet(name):

    print("Hello", name)


greet("Moin")


# =====================================================
# 9. *args AND **kwargs
# =====================================================

print("9. *args and **kwargs")


def decorator(function):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = function(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


print(add(10, 20))


# *args and **kwargs allow the decorator
# to work with different function arguments.


# =====================================================
# 10. REAL EXAMPLE - LOGIN CHECK
# =====================================================

print("10. Login Check")


def login_required(function):

    def wrapper(is_logged_in):

        if is_logged_in:

            function(is_logged_in)

        else:

            print("Please Login First")

    return wrapper


@login_required
def dashboard(is_logged_in):

    print("Welcome to Dashboard")


dashboard(True)

dashboard(False)


# =====================================================
# 11. REAL EXAMPLE - PERMISSION CHECK
# =====================================================

print("11. Permission Check")


def admin_required(function):

    def wrapper(role):

        if role == "admin":

            function(role)

        else:

            print("Access Denied")

    return wrapper


@admin_required
def admin_panel(role):

    print("Welcome to Admin Panel")


admin_panel("admin")

admin_panel("user")


# =====================================================
# 12. REAL EXAMPLE - LOGGING
# =====================================================

print("12. Logging")


def log_function(function):

    def wrapper(*args, **kwargs):

        print("Calling:", function.__name__)

        result = function(*args, **kwargs)

        print("Finished:", function.__name__)

        return result

    return wrapper


@log_function
def calculate_total(price, quantity):

    return price * quantity


print(calculate_total(500, 3))


# =====================================================
# 13. REAL EXAMPLE - EXECUTION TIME
# =====================================================

print("13. Execution Time")


import time


def execution_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper

@execution_time
def process_data():
    time.sleep(1)
    print("Data Processed")
process_data()


# =====================================================
# 14. MULTIPLE DECORATORS
# =====================================================

print("14. Multiple Decorators")


def decorator_one(function):
    def wrapper():
        print("Decorator One")
        function()
    return wrapper


def decorator_two(function):
    def wrapper():
        print("Decorator Two")
        function()
    return wrapper

@decorator_one
@decorator_two
def show():
    print("Original Function")

show()


# Equivalent to:
# show = decorator_one(decorator_two(show))


# =====================================================
# 15. DECORATOR WITH PARAMETERS
# =====================================================

print("15. Decorator with Parameters")


def repeat(times):

    def decorator(function):
        def wrapper():
            for _ in range(times):
                function()
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()


for i in range(3):
    print(i)

# =====================================================
# 19. @classmethod
# =====================================================

print("19. @classmethod")


class Employee:

    company = "AIZ INFOTECHS"

    @classmethod
    def show_company(cls):

        print(cls.company)


Employee.show_company()


# @classmethod receives cls.
#
# cls refers to the class.


# =====================================================
# 20. @staticmethod
# =====================================================

print("20. @staticmethod")


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))


# Static method does not require:
#
# self
# or
# cls


# =====================================================
# 21. DECORATOR FLOW
# =====================================================

print("21. Decorator Flow")


def check(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper


@check
def message():

    print("Hello")


message()


# FLOW:
#
# @check
#    ↓
# message = check(message)
#    ↓
# check receives original message()
#    ↓
# check returns wrapper()
#    ↓
# message now refers to wrapper
#    ↓
# message()
#    ↓
# wrapper()
#    ↓
# Before
#    ↓
# Original message()
#    ↓
# After


# =====================================================
# 22. SUMMARY
# =====================================================

print("22. Summary")

print("Decorator")
print("@decorator")
print("Wrapper Function")
print("*args")
print("**kwargs")
print("@classmethod")
print("@staticmethod")