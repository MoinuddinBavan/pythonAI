# =====================================================
# PYTHON INHERITANCE
# =====================================================

print("=" * 50)
print("Python Inheritance")
print("=" * 50)


# =====================================================
# 1. SIMPLE INHERITANCE
# =====================================================

print("1. Simple Inheritance")

class Person:

    def introduce(self):
        print("I am a Person")


class Student(Person):

    pass


student = Student()

student.introduce()


# =====================================================
# 2. PARENT CONSTRUCTOR
# =====================================================

print("2. Parent Constructor")

class Person:

    def __init__(self):

        print("Person Constructor")


class Student(Person):

    pass


student = Student()


# =====================================================
# 3. CHILD CONSTRUCTOR
# =====================================================

print("3. Child Constructor")

class Person:

    def __init__(self):

        print("Person Constructor")


class Student(Person):

    def __init__(self):

        print("Student Constructor")


student = Student()


# =====================================================
# 4. super()
# =====================================================

print("4. super()")

class Person:

    def __init__(self):

        print("Person Constructor")


class Student(Person):

    def __init__(self):

        super().__init__()

        print("Student Constructor")


student = Student()


# =====================================================
# 5. INHERIT INSTANCE VARIABLES
# =====================================================

print("5. Instance Variables")

class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    pass


student = Student("Moin")

print(student.name)


# =====================================================
# 6. INHERIT METHODS
# =====================================================

print("6. Inherit Methods")

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    pass


dog = Dog()

dog.sound()


# =====================================================
# 7. METHOD OVERRIDING
# =====================================================

print("7. Method Overriding")

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Bark")


dog = Dog()

dog.sound()


# =====================================================
# 8. MULTILEVEL INHERITANCE
# =====================================================

print("8. Multilevel Inheritance")

class A:

    def show(self):

        print("Class A")


class B(A):

    pass


class C(B):

    pass


obj = C()

obj.show()


# =====================================================
# 9. MULTIPLE INHERITANCE
# =====================================================

print("9. Multiple Inheritance")

class Father:

    def father(self):

        print("Father")


class Mother:

    def mother(self):

        print("Mother")


class Child(Father, Mother):

    pass


child = Child()

child.father()
child.mother()


# =====================================================
# 10. isinstance()
# =====================================================

print("10. isinstance()")

print(isinstance(child, Child))
print(isinstance(child, Father))
print(isinstance(child, Mother))


# =====================================================
# 11. issubclass()
# =====================================================

print("11. issubclass()")

print(issubclass(Child, Father))
print(issubclass(Dog, Animal))


# =====================================================
# 12. REAL EXAMPLE
# =====================================================

print("12. Student")

class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def study(self):

        print(self.name, "is studying.")


student = Student("Moin")

student.study()


# =====================================================
# 13. REAL EXAMPLE
# =====================================================

print("13. Employee")

class Employee:

    def login(self):

        print("Employee Login")


class Manager(Employee):

    def approve(self):

        print("Leave Approved")


manager = Manager()

manager.login()
manager.approve()


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Vehicle")

class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    pass


car = Car()

car.start()


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. AI Model")

class AIModel:

    def predict(self):

        print("Prediction Generated")


class ChatGPT(AIModel):

    pass


chatgpt = ChatGPT()

chatgpt.predict()


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. Payment")

class Payment:

    def pay(self):

        print("Payment Processing")


class UPI(Payment):

    pass


upi = UPI()

upi.pay()


# =====================================================
# 17. SUMMARY
# =====================================================

print("17. Summary")

print("Inheritance")
print("Parent Class")
print("Child Class")
print("super()")
print("Method Overriding")
print("Multilevel Inheritance")
print("Multiple Inheritance")
print("isinstance()")
print("issubclass()")


# NOTE:
#
# Parent Class
#        │
#        ▼
# Child Class
#
# Child class gets:
#
# ✔ Variables
# ✔ Methods
#
# without rewriting code.
#
# super()
# calls the parent class constructor or methods.
#
# Method Overriding means replacing the parent's method
# with a new implementation in the child class.
#
# Inheritance helps reuse code and is widely used in:
#
# ✔ Django Models
# ✔ FastAPI Classes
# ✔ TensorFlow
# ✔ PyTorch
# ✔ AI Agents