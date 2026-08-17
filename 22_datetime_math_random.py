# =====================================================
# DATETIME, MATH AND RANDOM
# =====================================================

print("=" * 50)
print("Datetime, Math and Random")
print("=" * 50)


# =====================================================
# 1. DATETIME MODULE
# =====================================================

print("1. Datetime Module")

import datetime

# datetime is Python's built-in module
# for working with dates and times.


# =====================================================
# 2. CURRENT DATE AND TIME
# =====================================================

print("2. Current Date and Time")

now = datetime.datetime.now()

print(now)


# Example:
#
# 2026-08-17 08:30:45.123456


# =====================================================
# 3. CURRENT DATE
# =====================================================

print("3. Current Date")

today = datetime.date.today()

print(today)


# Example:
#
# 2026-08-17


# =====================================================
# 4. DATE PARTS
# =====================================================

print("4. Date Parts")

today = datetime.date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# =====================================================
# 5. TIME PARTS
# =====================================================

print("5. Time Parts")

now = datetime.datetime.now()

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


# =====================================================
# 6. CREATE DATE
# =====================================================

print("6. Create Date")

date = datetime.date(
    2026,
    8,
    15
)

print(date)


# Format:
#
# datetime.date(
#     year,
#     month,
#     day
# )


# =====================================================
# 7. CREATE DATETIME
# =====================================================

print("7. Create Datetime")

meeting = datetime.datetime(
    2026,
    8,
    20,
    10,
    30
)

print(meeting)


# year
# month
# day
# hour
# minute


# =====================================================
# 8. strftime()
# =====================================================

print("8. strftime()")

now = datetime.datetime.now()

formatted = now.strftime(
    "%d-%m-%Y"
)

print(formatted)


# strftime()
# converts date/time into formatted STRING.


# =====================================================
# 9. DATE FORMATTING
# =====================================================

print("9. Date Formatting")

now = datetime.datetime.now()

print(
    now.strftime("%d/%m/%Y")
)

print(
    now.strftime("%d-%m-%Y")
)

print(
    now.strftime("%Y-%m-%d")
)

print(
    now.strftime("%d %B %Y")
)


# Common formats:
#
# %d → Day
# %m → Month number
# %Y → Full year
# %y → Short year
# %B → Full month name
# %b → Short month name
# %A → Full weekday name
# %a → Short weekday name
# %H → Hour (24-hour)
# %I → Hour (12-hour)
# %M → Minute
# %S → Second
# %p → AM / PM


# =====================================================
# 10. DATE AND TIME FORMATTING
# =====================================================

print("10. Date and Time Formatting")

now = datetime.datetime.now()

print(
    now.strftime(
        "%d-%m-%Y %H:%M:%S"
    )
)

print(
    now.strftime(
        "%d %B %Y %I:%M %p"
    )
)


# =====================================================
# 11. strptime()
# =====================================================

print("11. strptime()")

date_string = "20-08-2026"

date = datetime.datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(date)
print(type(date))


# strptime()
#
# STRING → DATETIME


# =====================================================
# 12. strftime() VS strptime()
# =====================================================

print("12. strftime vs strptime")

# strftime()
#
# DATETIME → STRING


# strptime()
#
# STRING → DATETIME


# =====================================================
# 13. TIMEDELTA
# =====================================================

print("13. timedelta")

today = datetime.date.today()

after_7_days = today + datetime.timedelta(
    days=7
)

print("Today:", today)
print("After 7 Days:", after_7_days)


# timedelta represents a duration.


# =====================================================
# 14. PREVIOUS DATE
# =====================================================

print("14. Previous Date")

today = datetime.date.today()

yesterday = today - datetime.timedelta(
    days=1
)

print(yesterday)


# =====================================================
# 15. DATE DIFFERENCE
# =====================================================

print("15. Date Difference")

start = datetime.date(
    2026,
    8,
    1
)

end = datetime.date(
    2026,
    8,
    20
)

difference = end - start

print(difference)
print(difference.days)


# =====================================================
# 16. REAL EXAMPLE - EXPIRY DATE
# =====================================================

print("16. Expiry Date")

purchase_date = datetime.date.today()

expiry_date = (
    purchase_date
    + datetime.timedelta(days=365)
)

print("Purchase:", purchase_date)
print("Expiry:", expiry_date)


# =====================================================
# MATH MODULE
# =====================================================

print("=" * 50)
print("Math Module")
print("=" * 50)


# =====================================================
# 17. IMPORT MATH
# =====================================================

print("17. Import Math")

import math


# =====================================================
# 18. math.ceil()
# =====================================================

print("18. math.ceil()")

number = 10.2

print(
    math.ceil(number)
)


# ceil()
# rounds UP.
#
# 10.2 → 11


# =====================================================
# 19. math.floor()
# =====================================================

print("19. math.floor()")

number = 10.9

print(
    math.floor(number)
)


# floor()
# rounds DOWN.
#
# 10.9 → 10


# =====================================================
# 20. round() VS ceil() VS floor()
# =====================================================

print("20. round vs ceil vs floor")

number = 10.6

print("round:", round(number))
print("ceil:", math.ceil(number))
print("floor:", math.floor(number))


# round()
# → Nearest integer
#
# ceil()
# → Always upward
#
# floor()
# → Always downward


# =====================================================
# 21. math.sqrt()
# =====================================================

print("21. math.sqrt()")

print(
    math.sqrt(64)
)


# Square root:
#
# 64 → 8


# =====================================================
# 22. math.pow()
# =====================================================

print("22. math.pow()")

print(
    math.pow(2, 3)
)


# 2³ = 8
#
# math.pow() returns float.


# =====================================================
# 23. math.factorial()
# =====================================================

print("23. math.factorial()")

print(
    math.factorial(5)
)


# 5!
#
# 5 × 4 × 3 × 2 × 1
#
# = 120


# =====================================================
# 24. math.pi
# =====================================================

print("24. math.pi")

print(math.pi)


# =====================================================
# 25. CIRCLE AREA
# =====================================================

print("25. Circle Area")

radius = 5

area = (
    math.pi
    * radius
    * radius
)

print(area)


# =====================================================
# 26. math.gcd()
# =====================================================

print("26. math.gcd()")

print(
    math.gcd(12, 18)
)


# Greatest Common Divisor
#
# 12 and 18 → 6


# =====================================================
# 27. math.lcm()
# =====================================================

print("27. math.lcm()")

print(
    math.lcm(4, 6)
)


# Least Common Multiple
#
# 4 and 6 → 12


# =====================================================
# 28. math.fabs()
# =====================================================

print("28. math.fabs()")

print(
    math.fabs(-50)
)


# Returns absolute value as float.
#
# -50 → 50.0


# =====================================================
# 29. math constants
# =====================================================

print("29. Math Constants")

print("PI:", math.pi)
print("E:", math.e)


# =====================================================
# 30. REAL EXAMPLE - TOKEN CHUNKS
# =====================================================

print("30. Token Chunks")

tokens = 500

chunk_size = 128

chunks = math.ceil(
    tokens / chunk_size
)

print(chunks)


# 500 / 128
# ≈ 3.90
#
# We need 4 chunks.
#
# ceil() → 4


# =====================================================
# RANDOM MODULE
# =====================================================

print("=" * 50)
print("Random Module")
print("=" * 50)


# =====================================================
# 31. IMPORT RANDOM
# =====================================================

print("31. Import Random")

import random


# =====================================================
# 32. random.random()
# =====================================================

print("32. random.random()")

print(
    random.random()
)


# Returns random float:
#
# 0.0 <= number < 1.0


# =====================================================
# 33. random.randint()
# =====================================================

print("33. random.randint()")

number = random.randint(
    1,
    10
)

print(number)


# Random integer from:
#
# 1 to 10
#
# Both included.


# =====================================================
# 34. random.randrange()
# =====================================================

print("34. random.randrange()")

number = random.randrange(
    1,
    10
)

print(number)


# Similar to range().
#
# Start included
# Stop excluded.
#
# Possible:
#
# 1 to 9


# =====================================================
# 35. randint() VS randrange()
# =====================================================

print("35. randint vs randrange")

print(
    random.randint(1, 10)
)

print(
    random.randrange(1, 10)
)


# randint(1, 10)
# → 1 through 10
#
# randrange(1, 10)
# → 1 through 9


# =====================================================
# 36. random.choice()
# =====================================================

print("36. random.choice()")

students = [
    "Moin",
    "Aamir",
    "Zaid"
]

winner = random.choice(
    students
)

print(winner)


# Selects one random item.


# =====================================================
# 37. random.choices()
# =====================================================

print("37. random.choices()")

students = [
    "Moin",
    "Aamir",
    "Zaid"
]

selected = random.choices(
    students,
    k=2
)

print(selected)


# Selects multiple random items.
#
# Duplicate values are possible.


# =====================================================
# 38. random.sample()
# =====================================================

print("38. random.sample()")

students = [
    "Moin",
    "Aamir",
    "Zaid",
    "Ahmed"
]

selected = random.sample(
    students,
    k=2
)

print(selected)


# Selects multiple UNIQUE items.


# =====================================================
# 39. choices() VS sample()
# =====================================================

print("39. choices vs sample")

# choices()
# → Duplicates possible
#
# sample()
# → Unique selection


# =====================================================
# 40. random.shuffle()
# =====================================================

print("40. random.shuffle()")

numbers = [
    1,
    2,
    3,
    4,
    5
]

random.shuffle(numbers)

print(numbers)


# shuffle()
# changes the original list order.


# =====================================================
# 41. random.uniform()
# =====================================================

print("41. random.uniform()")

number = random.uniform(
    1.5,
    5.5
)

print(number)


# Returns random float
# between given values.


# =====================================================
# 42. RANDOM OTP - LEARNING EXAMPLE
# =====================================================

print("42. Random OTP")

otp = random.randint(
    100000,
    999999
)

print(otp)


# NOTE:
#
# random is fine for learning,
# games and simulations.
#
# Do NOT use random for
# security-sensitive OTPs/passwords.
#
# Use secrets module instead.


# =====================================================
# 43. secrets MODULE
# =====================================================

print("43. secrets Module")

import secrets

otp = secrets.randbelow(
    900000
) + 100000

print(otp)


# secrets is designed for
# security-sensitive randomness.


# =====================================================
# 44. RANDOM PASSWORD CHARACTER
# =====================================================

print("44. Random Character")

characters = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
)

character = secrets.choice(
    characters
)

print(character)


# =====================================================
# 45. RANDOM PASSWORD
# =====================================================

print("45. Random Password")

characters = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
)

password = "".join(
    secrets.choice(characters)
    for _ in range(10)
)

print(password)


# =====================================================
# 46. REAL EXAMPLE - DICE
# =====================================================

print("46. Dice")

dice = random.randint(
    1,
    6
)

print("Dice:", dice)


# =====================================================
# 47. REAL EXAMPLE - RANDOM WINNER
# =====================================================

print("47. Random Winner")

students = [
    "Moin",
    "Aamir",
    "Zaid",
    "Ahmed"
]

winner = random.choice(
    students
)

print("Winner:", winner)


# =====================================================
# 48. SUMMARY - DATETIME
# =====================================================

print("48. Datetime Summary")

print("datetime.datetime.now()")
print("datetime.date.today()")
print("strftime()")
print("strptime()")
print("timedelta")


# =====================================================
# 49. SUMMARY - MATH
# =====================================================

print("49. Math Summary")

print("math.ceil()")
print("math.floor()")
print("math.sqrt()")
print("math.pow()")
print("math.factorial()")
print("math.pi")
print("math.gcd()")
print("math.lcm()")


# =====================================================
# 50. SUMMARY - RANDOM
# =====================================================

print("50. Random Summary")

print("random.random()")
print("random.randint()")
print("random.randrange()")
print("random.choice()")
print("random.choices()")
print("random.sample()")
print("random.shuffle()")
print("random.uniform()")
print("secrets → secure randomness")