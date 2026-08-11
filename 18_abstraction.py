# =====================================================
# PYTHON ABSTRACTION
# =====================================================

print("=" * 50)
print("Python Abstraction")
print("=" * 50)


# =====================================================
# 1. WHAT IS ABSTRACTION?
# =====================================================

print("1. Abstraction")

# Abstraction means:
#
# Hide unnecessary internal details
# and show only important functionality.
#
# Example:
#
# user.pay()
#
# User does not need to know
# every internal payment step.


# =====================================================
# 2. ABC MODULE
# =====================================================

print("2. ABC Module")


from abc import ABC, abstractmethod


# ABC = Abstract Base Class


# =====================================================
# 3. ABSTRACT CLASS
# =====================================================

print("3. Abstract Class")


class Payment(ABC):

    @abstractmethod
    def pay(self):

        pass


# Payment is an abstract class.


# =====================================================
# 4. CHILD IMPLEMENTATION
# =====================================================

print("4. Child Implementation")


class UPI(Payment):

    def pay(self):

        print("UPI Payment")


upi = UPI()

upi.pay()


# =====================================================
# 5. MULTIPLE CHILD CLASSES
# =====================================================

print("5. Multiple Implementations")


class Card(Payment):

    def pay(self):

        print("Card Payment")


class Cash(Payment):

    def pay(self):

        print("Cash Payment")


card = Card()
cash = Cash()

card.pay()
cash.pay()


# =====================================================
# 6. ABSTRACT CLASS CANNOT BE USED DIRECTLY
# =====================================================

print("6. Abstract Object")

# payment = Payment()
#
# This will give an error because
# Payment contains an abstract method.


# =====================================================
# 7. REAL EXAMPLE - NOTIFICATION
# =====================================================

print("7. Notification")


class Notification(ABC):

    @abstractmethod
    def send(self):

        pass


class EmailNotification(Notification):

    def send(self):

        print("Email Sent")


class SMSNotification(Notification):

    def send(self):

        print("SMS Sent")


email = EmailNotification()
sms = SMSNotification()

email.send()
sms.send()


# =====================================================
# 8. REAL EXAMPLE - AI MODEL
# =====================================================

print("8. AI Model")


class AIModel(ABC):

    @abstractmethod
    def generate(self, prompt):

        pass


class CloudAI(AIModel):

    def generate(self, prompt):

        return f"Cloud AI: {prompt}"


class LocalAI(AIModel):

    def generate(self, prompt):

        return f"Local AI: {prompt}"


cloud = CloudAI()
local = LocalAI()

print(
    cloud.generate(
        "Explain Python"
    )
)

print(
    local.generate(
        "Explain Python"
    )
)


# =====================================================
# 9. SUMMARY
# =====================================================

print("9. Summary")

print("Abstraction")
print("ABC")
print("Abstract Class")
print("@abstractmethod")
print("Implementation")
print("Hide Internal Details")