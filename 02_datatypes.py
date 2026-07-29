# =====================================================
# PYTHON DATA TYPES
# =====================================================

print("=" * 50)
print("Python Data Types")
print("=" * 50)


# Data Types in Python
# Numeric 
# 1)Integer => age = 32
# 2)Float => price = 499.99
# 3)Complex => a = 1 + 2j

# Boolean 
# 1) bool True => 
# 2) False

# Text
# 1) string => name = "Moin"

# Sequence
# 1) List => [1, 2, "Zaid", 2.90, True]
# 2) Tuple => (1, 2, "Zaid", 2.90, True)
# 3) Range => range(10)

# Mapping
# 1) Dict => {"name": "Moin", "age": 32}

# Set
# 1) set => {1, 2, 3}
# 2) frozenset => frozenset({1, 2, 3})

# Binary
# 1) bytes => b"hello"
# 2) bytearray => bytearray(b"hello")
# 3) memoryview => memoryview(b"hello")

# Special
# 1) NoneType => None


# =====================================================
# 1. INTEGER (int)
# =====================================================

print("1. Integer")

age = 20

print(age)
print(type(age))

# print(type(age))


# =====================================================
# 2. FLOAT (float)
# =====================================================

print("2. Float")

price = 599.99

print(price)
print(type(price))


# =====================================================
# 3. STRING (str)
# =====================================================

print("3. String")

company = "AIZ INFOTECHS"

print(company)
print(type(company))


# =====================================================
# 4. BOOLEAN (bool)
# =====================================================

print("4. Boolean")

is_admin = True

print(is_admin)
print(type(is_admin))


# =====================================================
# 5. NONE TYPE
# =====================================================

print("5. None")

profile_image = None

print(profile_image)
print(type(profile_image))


# =====================================================
# 6. CHECK DATA TYPE
# =====================================================

print("6. type()")

print(type(100))
print(type(10.5))
print(type("Python"))
print(type(True))
print(type(None))


# =====================================================
# 7. TYPE CONVERSION  String to Number
# =====================================================

print("7. Type Conversion")

number = "100"

print(type(number))

number = int(number)

print(number)
print(type(number))


# =====================================================
# 8. INTEGER TO FLOAT
# =====================================================

print("8. Integer to Float")

marks = 85

print(float(marks))


# =====================================================
# 9. FLOAT TO INTEGER
# =====================================================

print("9. Float to Integer")

salary = 45899.95

print(int(salary))


# =====================================================
# 10. INTEGER TO STRING
# =====================================================

print("10. Integer to String")

otp = 123456

otp = str(otp)

print(otp)
print(type(otp))


# =====================================================
# 11. STRING TO FLOAT
# =====================================================

print("11. String to Float")

price = "599.75"

price = float(price)

print(price)
print(type(price))


# =====================================================
# 12. Sequence (List, Tuple, Range) 
# =====================================================
# List => []
fruits = ["Mango", "banana", "Apple", "Grapes"]
print(fruits)
print(fruits[0])  # Accessing first element
print(fruits[1])  # Accessing second element
print(fruits[-1])  # Accessing last element
print(fruits[-2])  # Accessing second last element
print(fruits[1:3])  # Accessing elements from index 1 to 2


# =====================================================
# 13. Mapping (Dictionary) 
# =====================================================
# Dict => {}
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# Access data by key
print(student["name"])  # "Alice"
print(student.get("age"))  # 25