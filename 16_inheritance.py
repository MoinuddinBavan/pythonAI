# =====================================================
# PYTHON INHERITANCE
# =====================================================

print("=" * 50)
print("Python Inheritance")
print("=" * 50)


# =====================================================
# 1. WHAT IS INHERITANCE?
# =====================================================

print("1. Inheritance")

# Inheritance allows a child class
# to reuse properties and methods
# from a parent class.


# =====================================================
# 2. SIMPLE INHERITANCE
# =====================================================

print("2. Simple Inheritance")


class Person:

    def introduce(self):

        print("I am a Person")


class Student(Person):

    pass


student = Student()

student.introduce()


# =====================================================
# 3. PARENT AND CHILD
# =====================================================

print("3. Parent and Child")


# Person  -> Parent Class
# Student -> Child Class


# =====================================================
# 4. INHERIT CONSTRUCTOR
# =====================================================

print("4. Constructor")


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    pass


student = Student("Moin")

print(student.name)


# =====================================================
# 5. super()
# =====================================================

print("5. super()")


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, marks):

        super().__init__(name)

        self.marks = marks


student = Student(
    "Moin",
    90
)

print(student.name)
print(student.marks)


# =====================================================
# 6. INHERIT METHODS
# =====================================================

print("6. Inherit Methods")


class Employee:

    def login(self):

        print("Employee Login")


class Manager(Employee):

    def approve_leave(self):

        print("Leave Approved")


manager = Manager()

manager.login()
manager.approve_leave()


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

    def show_a(self):

        print("Class A")


class B(A):

    pass


class C(B):

    pass


obj = C()

obj.show_a()


# =====================================================
# 9. MULTIPLE INHERITANCE
# =====================================================

print("9. Multiple Inheritance")


class Camera:

    def camera(self):

        print("Camera")


class GPS:

    def gps(self):

        print("GPS")


class Phone(Camera, GPS):

    pass


phone = Phone()

phone.camera()
phone.gps()


# =====================================================
# 10. REAL EXAMPLE - AI MODEL
# =====================================================

print("10. AI Model")


class AIModel:

    def predict(self):

        print("Generating Prediction")


class ChatModel(AIModel):

    def chat(self):

        print("Generating Chat Response")


model = ChatModel()

model.predict()
model.chat()


# =====================================================
# 11. SUMMARY
# =====================================================

print("11. Summary")

print("Inheritance")
print("Parent Class")
print("Child Class")
print("super()")
print("Method Overriding")
print("Multilevel Inheritance")
print("Multiple Inheritance")