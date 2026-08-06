# =====================================================
# PYTHON OBJECT ORIENTED PROGRAMMING (OOP)
# =====================================================

print("=" * 50)
print("Python OOP")
print("=" * 50)


# =====================================================
# 1. CREATE CLASS
# =====================================================

print("1. Create Class")

class Student:

    pass

print(Student)


# =====================================================
# 2. CREATE OBJECT
# =====================================================

print("2. Create Object")

class Student:

    pass

student1 = Student()

print(student1)


# =====================================================
# 3. CONSTRUCTOR (__init__)
# =====================================================

print("3. Constructor")

class Student:

    def __init__(self):

        print("Constructor Called")

student = Student()


# =====================================================
# 4. INSTANCE VARIABLES
# =====================================================

print("4. Instance Variables")

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student = Student("Moin", 32)

print(student.name)
print(student.age)


# =====================================================
# 5. INSTANCE METHODS
# =====================================================

print("5. Instance Methods")

class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print(self.name)

student = Student("Aamir")

student.display()


# =====================================================
# 6. MULTIPLE OBJECTS
# =====================================================

print("6. Multiple Objects")

class Student:

    def __init__(self, name):

        self.name = name

student1 = Student("Moin")
student2 = Student("Yasin")

print(student1.name)
print(student2.name)


# =====================================================
# 7. MODIFY OBJECT VALUE
# =====================================================

print("7. Modify Object")

student1.name = "Akib"

print(student1.name)


# =====================================================
# 8. DELETE OBJECT PROPERTY
# =====================================================

print("8. Delete Property")

class Employee:

    def __init__(self):

        self.salary = 50000

employee = Employee()

print(employee.salary)

del employee.salary

# print(employee.salary)


# =====================================================
# 9. DELETE OBJECT
# =====================================================

print("9. Delete Object")

class Product:

    pass

product = Product()

del product

# print(product)


# =====================================================
# 10. CLASS VARIABLE
# =====================================================

print("10. Class Variable")

class Company:

    company_name = "AIZ INFOTECHS"

print(Company.company_name)


# =====================================================
# 11. CLASS METHOD
# =====================================================

print("11. Class Method")

class Company:

    company = "AIZ"

    @classmethod
    def display(cls):

        print(cls.company)

Company.display()


# =====================================================
# 12. STATIC METHOD
# =====================================================

print("12. Static Method")

class Math:

    @staticmethod
    def add(a, b):

        return a + b

print(Math.add(10, 20))


# =====================================================
# 13. __str__()
# =====================================================

print("13. __str__")

class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name

student = Student("Moin")

print(student)


# =====================================================
# 14. __repr__()
# =====================================================

print("14. __repr__")

class Product:

    def __repr__(self):

        return "Product Object"

product = Product()

print(product)


# =====================================================
# 15. SELF KEYWORD
# =====================================================

print("15. self Keyword")

class User:

    def __init__(self, name):

        self.name = name

    def display(self):

        print(self.name)

user = User("Moin")

user.display()


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. Student")

class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def result(self):

        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")

student = Student("Moin", 91)

student.result()


# =====================================================
# 17. REAL EXAMPLE
# =====================================================

print("17. Employee")

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def bonus(self):

        return self.salary * 0.10

employee = Employee("Aamir", 50000)

print(employee.bonus())


# =====================================================
# 18. REAL EXAMPLE
# =====================================================

print("18. Product")

class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def discount(self):

        return self.price * 0.90

product = Product("Laptop", 75000)

print(product.discount())


# =====================================================
# 19. REAL EXAMPLE
# =====================================================

print("19. AI Model")

class AIModel:

    def __init__(self, model, temperature):

        self.model = model
        self.temperature = temperature

    def info(self):

        print(self.model)
        print(self.temperature)

ai = AIModel("GPT-5", 0.7)

ai.info()


# =====================================================
# 20. SUMMARY
# =====================================================

print("20. Summary")

print("Class")
print("Object")
print("Constructor")
print("self")
print("Instance Variable")
print("Instance Method")
print("Class Variable")
print("Class Method")
print("Static Method")
print("__str__()")
print("__repr__()")

# NOTE:
#
# JavaScript              Python
#
# class User {}      -> class User:
#
# constructor()      -> __init__()
#
# this.name          -> self.name
#
# static             -> @staticmethod
#
# OOP is the foundation of:
#
# ✔ Django
# ✔ FastAPI
# ✔ Flask
# ✔ TensorFlow
# ✔ PyTorch
# ✔ LangChain
# ✔ AI Agents
#
# Every major Python framework uses OOP.