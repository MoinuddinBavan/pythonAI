# =====================================================
# PYTHON ITERATORS & GENERATORS
# =====================================================

print("=" * 50)
print("Python Iterators & Generators")
print("=" * 50)


# =====================================================
# 1. ITERABLE
# =====================================================

print("1. Iterable")

students = ["Moin", "Aamir", "Zaid"]

for student in students:
    print(student)


# =====================================================
# 2. iter()
# =====================================================

print("2. iter()")

students = ["Moin", "Aamir", "Zaid"]

iterator = iter(students)

print(iterator)


# =====================================================
# 3. next()
# =====================================================

print("3. next()")

iterator = iter(students)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# =====================================================
# 4. StopIteration
# =====================================================

print("4. StopIteration")

iterator = iter([10, 20])

print(next(iterator))
print(next(iterator))

# print(next(iterator))
# Raises StopIteration


# =====================================================
# 5. STRING ITERATOR
# =====================================================

print("5. String Iterator")

iterator = iter("AIZ")

print(next(iterator))
print(next(iterator))
print(next(iterator))


# =====================================================
# 6. GENERATOR
# =====================================================

# yield = Give one value, pause, remember where you were, and continue later 

print("6. Generator")


def numbers():

    yield 1
    yield 2
    yield 3


result = numbers()

print(next(result))
print(next(result))
print(next(result))


# =====================================================
# 7. GENERATOR WITH LOOP
# =====================================================

print("7. Generator with Loop")


def generate_numbers():

    for number in range(1, 6):

        yield number


for number in generate_numbers():

    print(number)


# =====================================================
# 8. RETURN VS YIELD
# =====================================================

print("8. Return vs Yield")


def normal_function():
    return 10


def generator_function():
    yield 10
    yield 20
    yield 30


print(normal_function())

for value in generator_function():

    print(value)


# =====================================================
# 9. GENERATOR OBJECT
# =====================================================

print("9. Generator Object")


generator = generator_function()

print(generator)


# =====================================================
# 10. REAL EXAMPLE
# =====================================================

print("10. Student Generator")


def get_students():

    yield "Moin"
    yield "Aamir"
    yield "Zaid"


for student in get_students():

    print(student)


# =====================================================
# 11. REAL EXAMPLE - LARGE DATA
# =====================================================

print("11. Large Data")


def generate_ids():

    for user_id in range(1, 1000000):

        yield user_id


ids = generate_ids()

print(next(ids))
print(next(ids))
print(next(ids))


# =====================================================
# 12. SUMMARY
# =====================================================

print("12. Summary")

print("Iterable")
print("Iterator")
print("iter()")
print("next()")
print("StopIteration")
print("Generator")
print("yield")
print("return vs yield")