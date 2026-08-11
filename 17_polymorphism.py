# =====================================================
# PYTHON POLYMORPHISM
# =====================================================

print("=" * 50)
print("Python Polymorphism")
print("=" * 50)


# =====================================================
# 1. WHAT IS POLYMORPHISM?
# =====================================================

print("1. Polymorphism")

# Poly  = Many
# Morph = Forms
#
# Polymorphism means:
#
# Same method/interface
# Different behavior.


# =====================================================
# 2. SIMPLE EXAMPLE
# =====================================================

print("2. Simple Example")


class Dog:

    def sound(self):

        print("Bark")


class Cat:

    def sound(self):

        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# =====================================================
# 3. SAME METHOD DIFFERENT OBJECTS
# =====================================================

print("3. Same Method")


animals = [
    Dog(),
    Cat()
]

for animal in animals:

    animal.sound()


# =====================================================
# 4. POLYMORPHISM WITH INHERITANCE
# =====================================================

print("4. Inheritance Polymorphism")


class Payment:

    def pay(self):

        print("Processing Payment")


class UPI(Payment):

    def pay(self):

        print("Payment using UPI")


class Card(Payment):

    def pay(self):

        print("Payment using Card")


upi = UPI()
card = Card()

upi.pay()
card.pay()


# =====================================================
# 5. FUNCTION POLYMORPHISM
# =====================================================

print("5. Function Polymorphism")


def make_payment(payment):

    payment.pay()


make_payment(UPI())
make_payment(Card())


# =====================================================
# 6. BUILT-IN POLYMORPHISM
# =====================================================

print("6. Built-in Polymorphism")


print(len("Python"))

print(
    len(
        [10, 20, 30]
    )
)

print(
    len(
        {
            "name": "Moin",
            "age": 32
        }
    )
)


# Same len()
# Different object types.


# =====================================================
# 7. REAL EXAMPLE - NOTIFICATION
# =====================================================

print("7. Notification")


class Email:

    def send(self):

        print("Sending Email")


class SMS:

    def send(self):

        print("Sending SMS")


class WhatsApp:

    def send(self):

        print("Sending WhatsApp Message")


notifications = [
    Email(),
    SMS(),
    WhatsApp()
]

for notification in notifications:

    notification.send()


# =====================================================
# 8. REAL EXAMPLE - AI
# =====================================================

print("8. AI Example")


class OpenAIModel:

    def generate(self):

        print("OpenAI Response")


class LocalModel:

    def generate(self):

        print("Local Model Response")


models = [
    OpenAIModel(),
    LocalModel()
]

for model in models:

    model.generate()


# =====================================================
# 9. SUMMARY
# =====================================================

print("9. Summary")

print("Polymorphism")
print("Same Method")
print("Different Behavior")
print("Method Overriding")
print("Function Polymorphism")
print("Built-in Polymorphism")