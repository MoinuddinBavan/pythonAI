# =====================================================
# PYTHON ENCAPSULATION
# =====================================================

print("=" * 50)
print("Python Encapsulation")
print("=" * 50)


# =====================================================
# 1. WHAT IS ENCAPSULATION?
# =====================================================

print("1. Encapsulation")

# Encapsulation means:
#
# Keeping data and methods together
# inside a class and controlling
# access to internal data.


# =====================================================
# 2. NORMAL PUBLIC PROPERTY
# =====================================================

print("2. Public Property")


class Student:

    def __init__(self, marks):

        self.marks = marks


student = Student(90)

print(student.marks)

student.marks = 95

print(student.marks)


# =====================================================
# 3. PROTECTED CONVENTION
# =====================================================

print("3. Protected Property")


class Employee:

    def __init__(self, salary):

        self._salary = salary


employee = Employee(50000)

print(employee._salary)


# _salary means:
#
# "Internal use" by convention.
#
# Python does NOT strictly prevent access.


# =====================================================
# 4. PRIVATE PROPERTY
# =====================================================

print("4. Private Property")


class BankAccount:

    def __init__(self, balance):

        self.__balance = balance

    def show_balance(self):

        return self.__balance


account = BankAccount(10000)

print(account.show_balance())

# print(account.__balance)
# This will give an error.


# =====================================================
# 5. CONTROL DATA USING METHOD
# =====================================================

print("5. Control Data")


class BankAccount:

    def __init__(self, balance):

        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def show_balance(self):

        return self.__balance


account = BankAccount(10000)

account.deposit(5000)

print(account.show_balance())


# =====================================================
# 6. GETTER
# =====================================================

print("6. Getter")


class Employee:

    def __init__(self, salary):

        self.__salary = salary

    def get_salary(self):

        return self.__salary


employee = Employee(50000)

print(employee.get_salary())


# =====================================================
# 7. SETTER
# =====================================================

print("7. Setter")


class Employee:

    def __init__(self, salary):

        self.__salary = salary

    def get_salary(self):

        return self.__salary

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary


employee = Employee(50000)

employee.set_salary(60000)

print(employee.get_salary())


# =====================================================
# 8. PROPERTY DECORATOR
# =====================================================

print("8. @property")


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


product = Product(5000)

print(product.price)

product.price = 6000

print(product.price)


# =====================================================
# 9. REAL EXAMPLE - BANK
# =====================================================

print("9. Bank Example")


class BankAccount:

    def __init__(self, balance):

        self.__balance = balance

    def deposit(self, amount):

        if amount <= 0:
            return "Invalid Amount"

        self.__balance += amount

        return "Deposit Successful"

    def withdraw(self, amount):

        if amount > self.__balance:
            return "Insufficient Balance"

        self.__balance -= amount

        return "Withdrawal Successful"

    def get_balance(self):

        return self.__balance


account = BankAccount(10000)

print(account.deposit(5000))
print(account.withdraw(3000))
print(account.get_balance())


# =====================================================
# 10. SUMMARY
# =====================================================

print("10. Summary")

print("Encapsulation")
print("Public Property")
print("Protected Convention _name")
print("Private Property __name")
print("Getter")
print("Setter")
print("@property")