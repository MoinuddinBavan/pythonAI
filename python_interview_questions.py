# =====================================================
# PYTHON INTERVIEW QUESTIONS & ANSWERS
# BASICS TO DECORATORS
# =====================================================


# =====================================================
# 1. PYTHON BASICS & DATA TYPES
# =====================================================

# Q1. What is Python?
#
# Answer:
# Python is a high-level, interpreted, general-purpose
# programming language.
#
# It supports:
# - Procedural Programming
# - Object-Oriented Programming
# - Functional Programming


# Q2. Is Python compiled or interpreted?
#
# Answer:
# Python is commonly called an interpreted language.
#
# In CPython:
#
# Python Source Code
#       ↓
# Bytecode
#       ↓
# Python Virtual Machine
#       ↓
# Execution


# Q3. What are Python's main built-in data types?
#
# Answer:
#
# Numeric:
# int
# float
# complex
#
# Text:
# str
#
# Boolean:
# bool
#
# Sequence:
# list
# tuple
# range
#
# Set:
# set
# frozenset
#
# Mapping:
# dict
#
# Binary:
# bytes
# bytearray
# memoryview
#
# None:
# NoneType


# Q4. What is Dynamic Typing?
#
# Answer:
# Python determines the type at runtime.
#
# A variable can refer to objects of different types.

value = 100

value = "Python"

value = True


# Q5. What is Mutable vs Immutable?
#
# Answer:
#
# Mutable:
# Object can be changed after creation.
#
# Examples:
# list
# dict
# set
#
#
# Immutable:
# Object cannot be changed in place.
#
# Examples:
# int
# float
# bool
# str
# tuple
# frozenset


# Q6. Difference between == and is?
#
# Answer:
#
# == checks VALUE equality.
#
# is checks OBJECT IDENTITY.

a = [1, 2]
b = [1, 2]

# a == b
# True
#
# a is b
# False


# Q7. What is None?
#
# Answer:
# None represents absence of a value.
#
# Its type is NoneType.

result = None


# Q8. What does id() do?
#
# Answer:
# id() returns an integer that uniquely identifies
# an object during its lifetime.

number = 100

# print(id(number))


# =====================================================
# 2. OPERATORS
# =====================================================

# Q9. What are the main types of operators?
#
# Answer:
#
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Membership Operators
# Identity Operators
# Bitwise Operators


# Q10. Difference between / and //?
#
# Answer:
#
# /  = True Division
# // = Floor Division

# 10 / 3
# 3.333...

# 10 // 3
# 3


# Q11. Difference between and and or?
#
# Answer:
#
# and
# → Both conditions should be truthy.
#
# or
# → At least one condition should be truthy.


# Q12. What are Membership Operators?
#
# Answer:
#
# in
# not in

students = ["Moin", "Aamir"]

# "Moin" in students
# True


# Q13. What are Identity Operators?
#
# Answer:
#
# is
# is not
#
# They compare object identity.


# =====================================================
# 3. CONDITIONS
# =====================================================

# Q14. Explain if, elif and else.
#
# Answer:
#
# if
# → Checks first condition
#
# elif
# → Checks another condition
#
# else
# → Runs when previous conditions are false

marks = 75

if marks >= 80:
    grade = "A"

elif marks >= 60:
    grade = "B"

else:
    grade = "C"


# Q15. What are Falsy values in Python?
#
# Answer:
#
# False
# None
# 0
# 0.0
# ""
# []
# {}
# set()


# Q16. What is a Conditional / Ternary Expression?
#
# Answer:
# It provides a short form of if-else.

marks = 90

result = "Pass" if marks >= 35 else "Fail"


# =====================================================
# 4. LOOPS
# =====================================================

# Q17. Difference between for and while?
#
# Answer:
#
# for
# → Usually used to iterate over an iterable.
#
# while
# → Repeats while a condition is truthy.


# Q18. Difference between break, continue and pass?
#
# Answer:
#
# break
# → Exit loop immediately.
#
# continue
# → Skip current iteration.
#
# pass
# → Do nothing.
# → Used as placeholder.


# Q19. What does range() do?
#
# Answer:
# range() returns a range object representing
# a sequence of integers.
#
# Syntax:
#
# range(start, stop, step)


# Q20. What does enumerate() do?
#
# Answer:
# enumerate() provides index and value
# while iterating.

students = ["Moin", "Aamir"]

for index, student in enumerate(students):
    pass


# Q21. What does zip() do?
#
# Answer:
# zip() combines elements from multiple
# iterables position-by-position.

names = ["Moin", "Aamir"]
marks = [90, 80]

for name, mark in zip(names, marks):
    pass


# =====================================================
# 5. LIST, TUPLE, SET, DICTIONARY
# =====================================================

# Q22. What is a List?
#
# Answer:
# A list is an ordered and mutable collection.

students = ["Moin", "Aamir"]


# Q23. Difference between List and Tuple?
#
# Answer:
#
# List:
# Mutable
# []
#
# Tuple:
# Immutable
# ()


# Q24. Difference between append() and extend()?
#
# Answer:
#
# append()
# → Adds one object as a single item.
#
# extend()
# → Adds items from another iterable individually.

numbers = [1, 2]

# numbers.append([3, 4])
#
# Result:
# [1, 2, [3, 4]]


numbers = [1, 2]

# numbers.extend([3, 4])
#
# Result:
# [1, 2, 3, 4]


# Q25. Difference between remove() and pop()?
#
# Answer:
#
# remove(value)
# → Removes first matching value.
#
# pop(index)
# → Removes and RETURNS an item.
# → Default is last item.


# Q26. Why use Tuple instead of List?
#
# Answer:
# Use tuple when data should not be modified
# and an immutable sequence is appropriate.


# Q27. How do you create a one-item Tuple?
#
# Answer:

single = (10,)

# Comma is required.


# Q28. What is a Set?
#
# Answer:
# Set is a mutable collection of unique
# hashable elements.

numbers = {1, 2, 3}


# Q29. How can you remove duplicates from a List?
#
# Answer:

numbers = [1, 1, 2, 2, 3]

unique_numbers = list(set(numbers))

# Note:
# Do not rely on this method to preserve
# the original list order.


# Q30. What is a Dictionary?
#
# Answer:
# Dictionary stores data as key-value pairs.

student = {
    "name": "Moin",
    "marks": 90
}


# Q31. Difference between dict[key] and dict.get(key)?
#
# Answer:
#
# dictionary[key]
# → Raises KeyError if key doesn't exist.
#
# dictionary.get(key)
# → Returns None by default if key doesn't exist.
#
# You can also provide a default value.

student.get("age", 0)


# =====================================================
# 6. STRINGS
# =====================================================

# Q32. Are Strings Mutable?
#
# Answer:
# No.
# Strings are immutable.


# Q33. What is String Slicing?
#
# Answer:
#
# Syntax:
#
# string[start:stop:step]

text = "Python"

result = text[0:3]

# Pyt


# Q34. How do you reverse a String?
#
# Answer:

text = "Python"

reverse = text[::-1]

# nohtyP


# Q35. What is an f-string?
#
# Answer:
# f-string allows expressions and variables
# inside formatted strings.

name = "Moin"
age = 32

message = f"My name is {name} and age is {age}"


# =====================================================
# 7. FUNCTIONS
# =====================================================

# Q36. What is a Function?
#
# Answer:
# Function is a reusable block of code
# designed to perform a task.


def add(a, b):

    return a + b


# Q37. Difference between Parameter and Argument?
#
# Answer:


def greet(name):
    #     ↑
    # Parameter

    pass


# greet("Moin")
#       ↑
# Argument


# Q38. Difference between return and print()?
#
# Answer:
#
# print()
# → Displays output.
#
# return
# → Sends result back to caller.
# → Ends that function call.


# Q39. What is *args?
#
# Answer:
# *args allows variable number of
# positional arguments.
#
# Inside function:
# args is a tuple.


def total(*numbers):

    return sum(numbers)


# Q40. What is **kwargs?
#
# Answer:
# **kwargs allows variable number of
# keyword arguments.
#
# Inside function:
# kwargs is a dictionary.


def user(**data):

    return data


# Q41. Difference between *args and **kwargs?
#
# Answer:
#
# *args
# → Extra positional arguments
# → Tuple
#
# **kwargs
# → Extra keyword arguments
# → Dictionary


# Q42. What is Recursion?
#
# Answer:
# Recursion happens when a function calls itself.
#
# A base condition is required to stop recursion.


def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)


# Q43. What is a Lambda Function?
#
# Answer:
# Lambda is a small anonymous function
# written as an expression.

square = lambda x: x * x


# Common uses:
#
# sorted()
# map()
# filter()


# =====================================================
# 8. MODULES AND PACKAGES
# =====================================================

# Q44. What is a Module?
#
# Answer:
# A module is a Python file containing
# reusable Python code.
#
# Example:
#
# calculator.py


# Q45. What is a Package?
#
# Answer:
# A package organizes related Python modules
# into a directory structure.
#
# Traditional packages commonly contain:
#
# __init__.py


# Q46. What are different ways to import?
#
# Answer:

# import math

# from math import sqrt

# import math as m

# from math import sqrt as square_root


# Q47. What does this mean?
#
# if __name__ == "__main__":
#
# Answer:
# It checks whether the Python file is being
# executed directly rather than imported.


# =====================================================
# 9. FILE HANDLING
# =====================================================

# Q48. What are common File Modes?
#
# Answer:
#
# r → Read
# w → Write / Overwrite
# a → Append
# x → Create
# b → Binary
# t → Text
# + → Read and Write / Update


# Q49. Why use with open()?
#
# Answer:
# It automatically handles file cleanup
# and closes the file when the block finishes.

# with open("data.txt", "r") as file:
#     data = file.read()


# Q50. Difference between read(), readline()
# and readlines()?
#
# Answer:
#
# read()
# → Reads all or specified amount.
#
# readline()
# → Reads one line.
#
# readlines()
# → Returns lines as a list.


# Q51. Difference between JSON dump and dumps?
#
# Answer:
#
# json.dump()
# → Serialize JSON to file-like object.
#
# json.dumps()
# → Serialize JSON to string.
#
#
# json.load()
# → Read JSON from file-like object.
#
# json.loads()
# → Parse JSON from string.


# =====================================================
# 10. EXCEPTION HANDLING
# =====================================================

# Q52. What is Exception Handling?
#
# Answer:
# Exception handling allows a program
# to handle runtime errors gracefully.


# Q53. Explain try, except, else and finally.
#
# Answer:
#
# try
# → Code that may cause exception.
#
# except
# → Handles exception.
#
# else
# → Runs if no exception occurs.
#
# finally
# → Runs whether exception occurs or not.


# Q54. Why should we avoid bare except?
#
# Answer:
# Bare except catches almost everything.
#
# Prefer specific exceptions.
#
# Example:
#
# except ValueError:


# Q55. What does raise do?
#
# Answer:
# raise explicitly raises an exception.

age = 20

if age < 0:

    raise ValueError(
        "Age cannot be negative"
    )


# =====================================================
# 11. OOP BASICS
# =====================================================

# Q56. What is OOP?
#
# Answer:
# OOP means Object-Oriented Programming.
#
# It organizes programs around objects
# containing data and behavior.


# Q57. What is a Class?
#
# Answer:
# Class is a blueprint/type definition
# used to create objects.


class Student:
    pass


# Q58. What is an Object?
#
# Answer:
# Object is an instance of a class.

student = Student()

# Student
# → Class
#
# student
# → Object / Instance


# Q59. What is __init__()?
#
# Answer:
# __init__() is a special method used
# to initialize an object's starting data.


# Q60. What is self?
#
# Answer:
# self refers to the current object / instance.


# Q61. Instance Variable vs Class Variable?
#
# Answer:


class Employee:

    company = "AIZ INFOTECHS"
    # ↑
    # Class Variable

    def __init__(self, name):

        self.name = name
        #    ↑
        # Instance Variable


# Class Variable:
# → Associated with class.
# → Shared/default across objects.
#
# Instance Variable:
# → Belongs to individual object.
# → Can differ for each object.


# Q62. What is a Method?
#
# Answer:
# A method is a function defined
# inside a class.


# =====================================================
# 12. ENCAPSULATION
# =====================================================

# Q63. What is Encapsulation?
#
# Answer:
# Encapsulation means keeping data and methods
# together and controlling access to
# internal object data.


# Q64. Difference between _name and __name?
#
# Answer:
#
# _name
# → Internal-use convention.
# → Still directly accessible.
#
# __name
# → Name mangling.
# → Direct obj.__name normally fails.
#
# __name is NOT a security mechanism.


# Q65. What is @property?
#
# Answer:
# @property allows a method to behave
# like an attribute while keeping
# controlled logic behind it.


class Product:

    def __init__(self, price):

        self.__price = price

    @property
    def price(self):

        return self.__price


# product.price
#
# instead of:
#
# product.get_price()


# Q66. What is a Setter?
#
# Answer:
# Setter controls how a property
# can be changed.


class Product:

    def __init__(self, price):

        self.__price = price

    @property
    def price(self):

        return self.__price

    @price.setter
    def price(self, value):

        if value >= 0:

            self.__price = value


# =====================================================
# 13. INHERITANCE
# =====================================================

# Q67. What is Inheritance?
#
# Answer:
# Inheritance allows a child class to
# reuse or extend features of a parent class.


class Person:
    pass


class Student(Person):
    pass


# Person
# → Parent Class
#
# Student
# → Child Class


# Q68. What does super() do?
#
# Answer:
# super() gives access to behavior from
# the next class in Method Resolution Order.
#
# Common use:
#
# super().__init__(name)


# Q69. What is Method Overriding?
#
# Answer:
# Method overriding happens when a child
# class provides its own implementation
# of an inherited method.


class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Bark")


# Q70. What are common types of Inheritance?
#
# Answer:
#
# Single
# Multilevel
# Hierarchical
# Multiple
# Hybrid


# =====================================================
# 14. POLYMORPHISM
# =====================================================

# Q71. What is Polymorphism?
#
# Answer:
# Polymorphism means the same interface/method
# can behave differently for different objects.


class Dog:

    def sound(self):

        print("Bark")


class Cat:

    def sound(self):

        print("Meow")


# Same:
#
# sound()
#
# Different:
#
# Dog → Bark
# Cat → Meow


# Q72. Method Overriding vs Polymorphism?
#
# Answer:
#
# Method Overriding:
# → Child provides its own version
#   of parent method.
#
# Polymorphism:
# → Same interface can work with
#   different object types.
#
# Overriding is one common way
# to achieve polymorphism.


# =====================================================
# 15. ABSTRACTION
# =====================================================

# Q73. What is Abstraction?
#
# Answer:
# Abstraction means hiding unnecessary
# implementation details and exposing
# only the required interface.


# Q74. What is ABC?
#
# Answer:
# ABC means Abstract Base Class.
#
# It provides the structure for creating
# abstract classes.


from abc import ABC, abstractmethod


# Q75. What is @abstractmethod?
#
# Answer:
# @abstractmethod marks a method that
# concrete child classes must implement.


class Notification(ABC):

    @abstractmethod
    def send(self):

        pass


class EmailNotification(Notification):

    def send(self):

        print("Email Sent")


# Easy Remember:
#
# ABC
# → Rule Structure / Rule Book
#
# @abstractmethod
# → Compulsory Rule


# Q76. Can we create an object of an Abstract Class?
#
# Answer:
# Not when it still contains
# unimplemented abstract methods.
#
# Example:
#
# notification = Notification()
#
# TypeError


# =====================================================
# 16. ITERATORS AND GENERATORS
# =====================================================

# Q77. Difference between Iterable and Iterator?
#
# Answer:
#
# Iterable:
# → Object that can be iterated over.
#
# Examples:
# list
# tuple
# string
# dictionary
# set
# range
#
#
# Iterator:
# → Object that gives values one-by-one
#   using next().


# Q78. What do iter() and next() do?
#
# Answer:

students = ["Moin", "Aamir"]

iterator = iter(students)

# iter()
# → Gets/creates iterator.
#
# next()
# → Gets next value.


# Q79. What happens when an Iterator finishes?
#
# Answer:
#
# Python raises:
#
# StopIteration


# Q80. What is a Generator?
#
# Answer:
# Generator is an easy way to create
# an iterator using yield.


def numbers():

    yield 1
    yield 2
    yield 3


# Q81. Difference between return and yield?
#
# Answer:
#
# return
# → Returns result.
# → Function call ends.
#
# yield
# → Produces one value.
# → Pauses generator.
# → Remembers state.
# → Continues later.


# Q82. Why use Generators?
#
# Answer:
# Generators produce values lazily.
#
# Useful for:
#
# Large Files
# Large Datasets
# Data Processing
# Streaming
# ML Data Pipelines
#
# They avoid creating all results
# in memory at once.


# =====================================================
# 17. DECORATORS
# =====================================================

# Q83. What is a Decorator?
#
# Answer:
# Decorator adds or modifies behavior
# of another function without changing
# the main function's code.


# Q84. What does @decorator syntax mean?
#
# Answer:


# @my_decorator
# def greet():
#     print("Hello")


# It is roughly equivalent to:
#
# greet = my_decorator(greet)


# Q85. What is a Wrapper Function?
#
# Answer:
# Wrapper is an inner function used by
# a decorator to add behavior around
# the original function.


def decorator(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper


# Q86. Why use *args and **kwargs in Decorators?
#
# Answer:
# They allow wrapper to work with functions
# having different numbers/types of arguments.


def decorator(function):

    def wrapper(*args, **kwargs):

        return function(
            *args,
            **kwargs
        )

    return wrapper


# Q87. Why use functools.wraps?
#
# Answer:
# functools.wraps preserves metadata
# of the original function.
#
# Examples:
#
# __name__
# __doc__


from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(
            *args,
            **kwargs
        )

    return wrapper


# Q88. What are real-world uses of Decorators?
#
# Answer:
#
# Authentication
# Authorization
# Logging
# Execution Time
# Caching
# Validation
# Retry Logic
# API Routing


# =====================================================
# MOST IMPORTANT INTERVIEW QUESTIONS
# =====================================================

# MUST PREPARE THESE WITHOUT NOTES:


# 1.
# List vs Tuple?


# 2.
# Mutable vs Immutable?


# 3.
# == vs is?


# 4.
# *args vs **kwargs?


# 5.
# What is Generator?
# Why use yield?


# 6.
# Iterable vs Iterator?


# 7.
# What are Class and Object?


# 8.
# Instance Variable vs Class Variable?


# 9.
# Explain 4 Pillars of OOP.


# 10.
# What does super() do?


# 11.
# What are ABC and @abstractmethod?


# 12.
# What is a Decorator?


# 13.
# What is Method Overriding?


# 14.
# Encapsulation vs Abstraction?


# 15.
# What is Polymorphism?


# =====================================================
# 4 PILLARS QUICK REVISION
# =====================================================

# ENCAPSULATION
# ↓
# Control access to object data.


# INHERITANCE
# ↓
# Reuse / extend parent features.


# POLYMORPHISM
# ↓
# Same interface,
# different behavior.


# ABSTRACTION
# ↓
# Hide unnecessary
# implementation details.


# =====================================================
# DECORATOR QUICK REVISION
# =====================================================

# @decorator
#      ↓
# function = decorator(function)
#      ↓
# Decorator receives function
#      ↓
# Returns wrapper
#      ↓
# Wrapper adds extra behavior
#      ↓
# Original function still executes


# =====================================================
# END
# =====================================================