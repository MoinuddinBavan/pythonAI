# =====================================================
# PYTHON OOP BASICS
# =====================================================

print("=" * 50)
print("Python OOP Basics")
print("=" * 50)



# PYTHON OOP
# │
# ├── 14_oop_basics.py
# │   ├── Class
# │   ├── Object
# │   ├── __init__()
# │   ├── self
# │   ├── Properties
# │   └── Methods
# │
# ├── 15_encapsulation.py
# │   └── Protect / Control Data
# │
# ├── 16_inheritance.py
# │   └── Reuse Parent Features
# │
# ├── 17_polymorphism.py
# │   └── Same Method, Different Behavior
# │
# └── 18_abstraction.py
#     └── Hide Internal Complexity

# =====================================================
# 1. WHAT IS OOP?
# =====================================================

print("1. What is OOP?")

# OOP = Object-Oriented Programming
#
# OOP organizes programs using:
#
# Class
# Object
# Properties
# Methods


# =====================================================
# 2. CREATE CLASS
# =====================================================

print("2. Create Class")

class Student: # this is class
    pass


print(Student)


# =====================================================
# 3. CREATE OBJECT
# =====================================================

print("3. Create Object")


student1 = Student() # this is object (instance of Student class)

print(student1)

# =====================================================
# 4. OBJECT PROPERTIES
# =====================================================

class Car:
    color = "Red" # this is property
    brand = "Toyota" # this is property

car1 = Car() # this is object (instance of Car class)
print(car1.color, car1.brand)


# =====================================================
# 5. __init__() CONSTRUCTOR
# =====================================================

print("5. Constructor")


class Student:

    def __init__():
        print("Adding New Student into database")

s1 = Student() # this is object
print(s1)



# =====================================================
# 6. SELF
# =====================================================

print("6. self")


# self refers to the current object.
#
# student1:
# self.name = "Moin"
#
# student2:
# self.name = "Aamir"


class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


employee1 = Employee("Moin", 50000)
employee2 = Employee("Aamir", 60000)


print(employee1.name)
print(employee2.name)


# =====================================================
# 7. INSTANCE VARIABLES
# =====================================================

print("7. Instance Variables")


class Product:

    
    def __init__(self, name, price):

        self.name = name
        self.price = price


product1 = Product("Laptop", 75000)
product2 = Product("Mouse", 1500)


print(product1.name, product1.price)
print(product2.name, product2.price)


# =====================================================
# 8. INSTANCE METHOD
# =====================================================

print("8. Instance Method")


class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def show_details(self):

        print("Name:", self.name)
        print("Marks:", self.marks)


student = Student("Moin", 90)

student.show_details()


# =====================================================
# 10. MULTIPLE METHODS
# =====================================================

print("10. Multiple Methods")


class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def show_balance(self):

        return self.balance


account = BankAccount("Moin", 10000)

account.deposit(5000)

print(account.show_balance())


# =====================================================
# 11. CLASS VARIABLE
# =====================================================

print("11. Class Variable")


class Employee:

    company = "AIZ INFOTECHS"

    def __init__(self, name):

        self.name = name


employee1 = Employee("Moin")
employee2 = Employee("Aamir")


print(employee1.company)
print(employee2.company)


# =====================================================
# 12. INSTANCE VS CLASS VARIABLE
# =====================================================

print("12. Instance vs Class Variable")


# company
#     -> Class Variable
#     -> Shared by all objects
#
# name
#     -> Instance Variable
#     -> Different for every object


# =====================================================
# 13. REAL EXAMPLE - STUDENT
# =====================================================

print("13. Student Example")


class Student:

    def __init__(self, name, marks, course):

        self.name = name
        self.marks = marks
        self.course = course

    def result(self):

        return "Pass" if self.marks >= 35 else "Fail"

    def show_details(self):

        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Course:", self.course)
        print("Result:", self.result())


student = Student(
    "Moin",
    90,
    "Python"
)

student.show_details()


# =====================================================
# 14. REAL EXAMPLE - AI MODEL
# =====================================================

print("14. AI Model Example")


class AIModel:

    def __init__(
        self,
        model_name,
        temperature
    ):

        self.model_name = model_name
        self.temperature = temperature

    def show_config(self):

        print("Model:", self.model_name)
        print("Temperature:", self.temperature)


model = AIModel(
    "GPT",
    0.7
)

model.show_config()


# =====================================================
# 15. SUMMARY
# =====================================================



class Student:                     # ← CLASS
                                   #   Blueprint / Template

    def __init__(self, name, marks):
        #      ↑
        #      └── self = CURRENT OBJECT

        self.name = name            # ← PROPERTY / INSTANCE VARIABLE
        self.marks = marks          # ← PROPERTY / INSTANCE VARIABLE

    def show_details(self):         # ← METHOD
                                   #   Function inside a class

        print(self.name)
        print(self.marks)


student1 = Student("Moin", 90)
#   ↑          ↑
#   │          └── Creating object from Student class
#   │
#   └── OBJECT / INSTANCE
#
# student1 is an object.
# student1 is also called an instance of Student class.


student1.show_details()
#   ↑          ↑
#   │          └── Calling METHOD
#   │
#   └── OBJECT


print("15. Summary")

print("OOP")
print("Class")
print("Object")
print("__init__()")
print("self")
print("Property")
print("Instance Variable")
print("Class Variable")
print("Method")