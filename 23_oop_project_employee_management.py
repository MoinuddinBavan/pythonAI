# =====================================================
# OOP MINI PROJECT
# EMPLOYEE MANAGEMENT SYSTEM
# =====================================================

print("=" * 50)
print("EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 50)


# =====================================================
# 1. EMPLOYEE CLASS
# =====================================================

class Employee:

    company = "AIZ INFOTECHS"

    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary


    @property
    def salary(self):

        return self.__salary


    @salary.setter
    def salary(self, salary):

        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")


    def show_details(self):

        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)


employee1 = Employee("Moin", 50000)

employee1.show_details()


employee1.salary = 60000

print("Updated Salary:", employee1.salary)