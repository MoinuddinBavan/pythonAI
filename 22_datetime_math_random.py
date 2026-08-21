# =====================================================
# 22. DATETIME, MATH AND RANDOM
# =====================================================

print("=" * 60)
print("Python - Datetime, Math and Random")
print("=" * 60)


# =====================================================
# IMPORTS
# =====================================================

from datetime import datetime, date, timedelta
import math
import random
import secrets


# =====================================================
# PART 1 - DATETIME
# =====================================================

print("\n" + "=" * 60)
print("PART 1 - DATETIME")
print("=" * 60)


# =====================================================
# 1. CURRENT DATE AND TIME
# =====================================================

print("\n1. Current Date and Time")

now = datetime.now()

print(now)


# datetime.now()
# ↓
# Gives current local date + time.
#
# Example:
#
# 2026-08-20 15:45:30.123456


# =====================================================
# 2. CURRENT DATE
# =====================================================

print("\n2. Current Date")

today = date.today()

print(today)


# Output format:
#
# YYYY-MM-DD


# =====================================================
# 3. DATE PARTS
# =====================================================

print("\n3. Date Parts")

today = date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# =====================================================
# 4. TIME PARTS
# =====================================================

print("\n4. Time Parts")

now = datetime.now()

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


# =====================================================
# 5. CREATE OUR OWN DATE
# =====================================================

print("\n5. Create Date")

independence_day = date( 2026, 8, 15 )

print(independence_day)


# Syntax:
#
# date(
#     year,
#     month,
#     day
# )


# =====================================================
# 6. CREATE OUR OWN DATETIME
# =====================================================

print("\n6. Create Datetime")

meeting = datetime(
    2026,
    8,
    25,
    10,
    30,
    0
)

print(meeting)


# Syntax:
#
# datetime(
#     year,
#     month,
#     day,
#     hour,
#     minute,
#     second
# )


# =====================================================
# 7. strftime()
# =====================================================

print("\n7. strftime()")

now = datetime.now()

formatted_date = now.strftime(
    "%d-%m-%Y"
)

print(formatted_date)


# strftime()
# ↓
# datetime → string
#
# Think:
#
# "format datetime as string"


# =====================================================
# 8. IMPORTANT DATE FORMAT CODES
# =====================================================

print("\n8. Date Formatting")

now = datetime.now()

print(now.strftime("%d-%m-%Y"))

print(now.strftime("%d/%m/%Y"))

print(now.strftime("%Y-%m-%d"))

print(now.strftime("%d %B %Y"))

print(now.strftime("%A, %d %B %Y"))

print(now.strftime("%I:%M %p"))


# IMPORTANT CODES:
#
# %d
# → Day
#
# %m
# → Month number
#
# %Y
# → Full year
#
# %y
# → Short year
#
# %B
# → Full month name
#
# %b
# → Short month name
#
# %A
# → Full weekday
#
# %a
# → Short weekday
#
# %H
# → 24-hour format
#
# %I
# → 12-hour format
#
# %M
# → Minute
#
# %S
# → Second
#
# %p
# → AM / PM


# =====================================================
# 9. strptime() # Parse String to DateTime
# =====================================================

print("\n9. strptime()")

date_string = "20-08-2026"

converted_date = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(converted_date)
print(type(converted_date))


# strptime()
# ↓
# string → datetime
#
# Think:
#
# "parse string into datetime"


# =====================================================
# 10. strftime() VS strptime()
# =====================================================

print("\n10. strftime vs strptime")

# strftime()
#
# datetime
#     ↓
# string


# strptime()
#
# string
#     ↓
# datetime


# Easy Remember:
#
# strftime
# → FORMAT date as STRING
#
# strptime
# → PARSE STRING into date/time


# =====================================================
# 11. timedelta
# =====================================================

print("\n11. timedelta")

today = date.today()

after_7_days = today + timedelta(
    days=7
)

print("Today:", today)
print("After 7 Days:", after_7_days)


# timedelta
# ↓
# Represents a duration.
#
# We can add or subtract:
#
# days
# seconds
# weeks
# hours
# minutes


# =====================================================
# 12. YESTERDAY
# =====================================================

print("\n12. Yesterday")

today = date.today()

yesterday = today - timedelta(
    days=1
)

print(yesterday)


# =====================================================
# 13. TOMORROW
# =====================================================

print("\n13. Tomorrow")

today = date.today()

tomorrow = today + timedelta(
    days=1
)

print(tomorrow)


# =====================================================
# 14. AFTER 30 DAYS
# =====================================================

print("\n14. After 30 Days")

today = date.today()

future_date = today + timedelta(
    days=30
)

print(future_date)


# =====================================================
# 15. DATE DIFFERENCE
# =====================================================

print("\n15. Date Difference")

start_date = date(
    2026,
    8,
    1
)

end_date = date(
    2026,
    8,
    20
)

difference = end_date - start_date

print(difference)

print(
    "Total Days:",
    difference.days
)


# =====================================================
# 16. COMPARE DATES
# =====================================================

print("\n16. Compare Dates")

today = date.today()

expiry_date = date(
    2026,
    12,
    31
)

if expiry_date > today:

    print("Subscription Active")

else:

    print("Subscription Expired")


# Dates can be compared using:
#
# >
# <
# >=
# <=
# ==
# !=


# =====================================================
# 17. REAL EXAMPLE - SUBSCRIPTION EXPIRY
# =====================================================

print("\n17. Subscription Expiry")

purchase_date = date.today()

expiry_date = (
    purchase_date
    + timedelta(days=365)
)

print(
    "Purchase Date:",
    purchase_date
)

print(
    "Expiry Date:",
    expiry_date
)


# =====================================================
# 18. REAL EXAMPLE - INVOICE DUE DATE
# =====================================================

print("\n18. Invoice Due Date")

invoice_date = date.today()

due_date = invoice_date + timedelta(
    days=15
)

print(
    "Invoice Date:",
    invoice_date
)

print(
    "Due Date:",
    due_date
)


# =====================================================
# 19. REAL EXAMPLE - CHECK EXPIRED
# =====================================================

print("\n19. Check Expired")

expiry_date = date(
    2026,
    8,
    10
)

today = date.today()

if today > expiry_date:

    print("Expired")

elif today == expiry_date:

    print("Expires Today")

else:

    print("Active")


# =====================================================
# PART 2 - MATH MODULE
# =====================================================

print("\n" + "=" * 60)
print("PART 2 - MATH MODULE")
print("=" * 60)


# =====================================================
# 20. math.ceil()
# =====================================================

print("\n20. math.ceil()")

number = 10.2

result = math.ceil(number)

print(result)


# ceil()
# ↓
# Round UP
#
# 10.2
# ↓
# 11


# =====================================================
# 21. math.floor()
# =====================================================

print("\n21. math.floor()")

number = 10.9

result = math.floor(number)

print(result)


# floor()
# ↓
# Round DOWN
#
# 10.9
# ↓
# 10


# =====================================================
# 22. round() VS ceil() VS floor()
# =====================================================

print("\n22. round vs ceil vs floor")

number = 10.6

print(
    "round:",
    round(number)
)

print(
    "ceil:",
    math.ceil(number)
)

print(
    "floor:",
    math.floor(number)
)


# round()
# → nearest
#
# ceil()
# → upward
#
# floor()
# → downward


# =====================================================
# 23. math.sqrt()
# =====================================================

print("\n23. math.sqrt()")

result = math.sqrt(64)

print(result)


# sqrt()
# ↓
# Square Root
#
# √64 = 8


# =====================================================
# 24. math.pow() # 2³ = 2 × 2 × 2 = 8
# =====================================================

print("\n24. math.pow()")

result = math.pow(
    2,
    3
)

print(result)


# 2 power 3
#
# 2 × 2 × 2
#
# = 8


# math.pow()
# returns float.
#
# 8.0


# =====================================================
# 25. ** POWER OPERATOR
# =====================================================

print("\n25. Power Operator")

result = 2 ** 3

print(result)


# 2 ** 3
# ↓
# 8


# Difference:
#
# math.pow(2, 3)
# → 8.0
#
# 2 ** 3
# → 8


# =====================================================
# 26. math.factorial()
# =====================================================

print("\n26. Factorial")

result = math.factorial(5)

print(result)


# 5!
#
# 5 × 4 × 3 × 2 × 1
#
# = 120


# =====================================================
# 27. math.pi
# =====================================================

print("\n27. PI")

print(math.pi)


# PI approximately:
#
# 3.141592...


# =====================================================
# 28. REAL EXAMPLE - CIRCLE AREA
# =====================================================

print("\n28. Circle Area")

radius = 5

area = (
    math.pi
    * radius
    * radius
)

print(
    "Area:",
    area
)


# Formula:
#
# π × r²


# =====================================================
# 29. math.gcd() # Greatest Common Divisor
# =====================================================

print("\n29. GCD")

result = math.gcd(
    12,
    18
)

print(result)


# GCD
# ↓
# Greatest Common Divisor
#
# 12 and 18
# ↓
# 6


# =====================================================
# 30. math.lcm()
# =====================================================

print("\n30. LCM")

result = math.lcm(
    4,
    6
)

print(result)


# LCM
# ↓
# Least Common Multiple
#
# 4 and 6
# ↓
# 12


# =====================================================
# 31. abs() VS math.fabs()
# =====================================================

print("\n31. abs vs fabs")

print(
    abs(-50)
)

print(
    math.fabs(-50)
)


# abs(-50)
# → 50
#
# math.fabs(-50)
# → 50.0


# =====================================================
# 32. REAL EXAMPLE - PAGE COUNT
# =====================================================

print("\n32. Page Count")

records = 103

records_per_page = 10

total_pages = math.ceil(
    records / records_per_page
)

print(
    "Total Pages:",
    total_pages
)


# 103 records
#
# 10 records/page
#
# Need:
#
# 11 pages


# =====================================================
# 33. REAL AI EXAMPLE - TOKEN CHUNKS
# =====================================================

print("\n33. AI Token Chunks")

total_tokens = 1000

chunk_size = 256

total_chunks = math.ceil(
    total_tokens / chunk_size
)

print(
    "Total Chunks:",
    total_chunks
)


# Useful later in:
#
# AI
# RAG
# text chunking
# data processing


# =====================================================
# PART 3 - RANDOM MODULE
# =====================================================

print("\n" + "=" * 60)
print("PART 3 - RANDOM MODULE")
print("=" * 60)


# =====================================================
# 34. random.random()
# =====================================================

print("\n34. random.random()")

number = random.random()

print(number)


# Gives float:
#
# 0.0 <= value < 1.0


# =====================================================
# 35. random.randint()
# =====================================================

print("\n35. random.randint()")

number = random.randint(
    1,
    10
)

print(number)


# randint(1, 10)
#
# Both included.
#
# Possible:
#
# 1 through 10


# =====================================================
# 36. random.randrange()
# =====================================================

print("\n36. random.randrange()")

number = random.randrange(
    1,
    10
)

print(number)


# Start included.
# Stop excluded.
#
# Possible:
#
# 1 through 9


# =====================================================
# 37. randint() VS randrange()
# =====================================================

print("\n37. randint vs randrange")

# randint(1, 10)
#
# 1 through 10


# randrange(1, 10)
#
# 1 through 9


# =====================================================
# 38. random.choice()
# =====================================================

print("\n38. random.choice()")

students = [
    "Moin",
    "Aamir",
    "Zaid",
    "Ahmed"
]

winner = random.choice(
    students
)

print(
    "Winner:",
    winner
)


# choice()
# ↓
# Select ONE random item.


# =====================================================
# 39. random.choices()
# =====================================================

print("\n39. random.choices()")

students = [
    "Moin",
    "Aamir",
    "Zaid",
    "Ahmed"
]

selected = random.choices(
    students,
    k=3
)

print(selected)


# choices()
#
# Select multiple values.
#
# IMPORTANT:
#
# Duplicate values ARE possible.


# =====================================================
# 40. random.sample()
# =====================================================

print("\n40. random.sample()")

students = [
    "Moin",
    "Aamir",
    "Zaid",
    "Ahmed"
]

selected = random.sample(
    students,
    k=3
)

print(selected)


# sample()
#
# Select multiple UNIQUE items.
#
# No duplicate selection.


# =====================================================
# 41. choices() VS sample()
# =====================================================

print("\n41. choices vs sample")

# choices()
# ↓
# Duplicate possible


# sample()
# ↓
# Unique selection


# =====================================================
# 42. random.shuffle()
# =====================================================

print("\n42. random.shuffle()")

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
# ↓
# Changes the ORIGINAL list.


# =====================================================
# 43. random.uniform()
# =====================================================

print("\n43. random.uniform()")

price = random.uniform(
    100,
    500
)

print(price)


# Gives random FLOAT
# between given numbers.


# =====================================================
# 44. RANDOM DICE
# =====================================================

print("\n44. Random Dice")

dice = random.randint(
    1,
    6
)

print(
    "Dice:",
    dice
)


# =====================================================
# 45. RANDOM STUDENT
# =====================================================

print("\n45. Random Student")

students = [
    "Moin",
    "Aamir",
    "Zaid",
    "Ahmed"
]

student = random.choice(
    students
)

print(
    "Selected Student:",
    student
)


# =====================================================
# 46. LEARNING OTP USING random
# =====================================================

print("\n46. Random OTP - Learning Only")

otp = random.randint(
    100000,
    999999
)

print(otp)


# IMPORTANT:
#
# random is NOT recommended
# for security-sensitive OTPs,
# passwords or security tokens.
#
# For security:
#
# use secrets module.


# =====================================================
# PART 4 - SECRETS MODULE
# =====================================================

print("\n" + "=" * 60)
print("PART 4 - SECRETS MODULE")
print("=" * 60)


# =====================================================
# 47. secrets.randbelow()
# =====================================================

print("\n47. Secure Random Number")

number = secrets.randbelow(
    100
)

print(number)


# randbelow(100)
#
# Possible:
#
# 0 through 99


# =====================================================
# 48. SECURE 6-DIGIT OTP-STYLE CODE
# =====================================================

print("\n48. Secure 6-Digit Code")

otp = (
    secrets.randbelow(900000)
    + 100000
)

print(otp)


# Why?
#
# secrets.randbelow(900000)
#
# gives:
#
# 0 to 899999
#
# Then:
#
# + 100000
#
# gives:
#
# 100000 to 999999


# =====================================================
# 49. secrets.choice()
# =====================================================

print("\n49. secrets.choice()")

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
# 50. SECURE PASSWORD
# =====================================================

print("\n50. Secure Password")

characters = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%"
)

password = "".join(
    secrets.choice(characters)
    for _ in range(12)
)

print(
    "Password:",
    password
)


# =====================================================
# IMPORTANT NEW SYNTAX
# =====================================================

# "".join(...)
#
# join()
# combines multiple strings
# into ONE string.


# Example:
#
# letters = ["A", "B", "C"]
#
# "".join(letters)
#
# ABC


# =====================================================
# WHAT IS THIS?
#
# for _ in range(12)
# =====================================================

# _ is just a variable name.
#
# We commonly use _
# when we don't need the loop value.


# Example:
#
# for _ in range(3):
#     print("Hello")
#
#
# Output:
#
# Hello
# Hello
# Hello


# In password generation:
#
# repeat 12 times
#      ↓
# choose one random character
#      ↓
# join all characters
#      ↓
# 12-character password


# =====================================================
# 51. random VS secrets
# =====================================================

print("\n51. random vs secrets")

# random
# ↓
# General-purpose randomness.
#
# Use for:
#
# Games
# Testing
# Simulations
# Random student selection
# Sample data


# secrets
# ↓
# Security-sensitive randomness.
#
# Use for:
#
# Tokens
# Passwords
# Secure codes
# Reset tokens
# Authentication-related values


# =====================================================
# QUICK REVISION
# =====================================================

print("\n" + "=" * 60)
print("QUICK REVISION")
print("=" * 60)


# =====================================================
# DATETIME
# =====================================================

# datetime.now()
# → Current date + time


# date.today()
# → Current date


# strftime()
# → datetime → string


# strptime()
# → string → datetime


# timedelta()
# → Add / subtract durations


# =====================================================
# MATH
# =====================================================

# math.ceil()
# → Round UP


# math.floor()
# → Round DOWN


# math.sqrt()
# → Square root


# math.pow()
# → Power


# math.factorial()
# → Factorial


# math.pi
# → PI


# math.gcd()
# → Greatest Common Divisor


# math.lcm()
# → Least Common Multiple


# =====================================================
# RANDOM
# =====================================================

# random.random()
# → Random float 0 to less than 1


# random.randint()
# → Both start and end included


# random.randrange()
# → End excluded


# random.choice()
# → One item


# random.choices()
# → Multiple items
# → Duplicate possible


# random.sample()
# → Multiple unique items


# random.shuffle()
# → Shuffle original list


# random.uniform()
# → Random float in range


# =====================================================
# SECRETS
# =====================================================

# secrets.randbelow()
# → Secure random integer


# secrets.choice()
# → Secure random choice


# Use secrets instead of random
# for security-sensitive values.


# =====================================================
# INTERVIEW QUESTIONS & ANSWERS
# =====================================================

print("\n" + "=" * 60)
print("INTERVIEW QUESTIONS")
print("=" * 60)


# =====================================================
# Q1. What is the datetime module?
# =====================================================

# Answer:
# datetime is a Python standard-library module
# used for working with dates and times.


# =====================================================
# Q2. Difference between date and datetime?
# =====================================================

# Answer:
#
# date
# → Stores mainly:
#   year, month, day
#
# datetime
# → Stores:
#   year, month, day,
#   hour, minute, second,
#   microsecond


# =====================================================
# Q3. What is datetime.now()?
# =====================================================

# Answer:
# datetime.now() returns the current
# local date and time.


# =====================================================
# Q4. What is date.today()?
# =====================================================

# Answer:
# date.today() returns the current
# local calendar date.


# =====================================================
# Q5. Difference between strftime() and strptime()?
# =====================================================

# Answer:
#
# strftime()
# → datetime to string
#
# strptime()
# → string to datetime


# Easy:
#
# FORMAT TIME
# → strftime
#
# PARSE TIME
# → strptime


# =====================================================
# Q6. What is timedelta?
# =====================================================

# Answer:
# timedelta represents a duration
# or difference between dates/times.
#
# It is commonly used to:
#
# add days
# subtract days
# calculate expiry
# calculate due date


# =====================================================
# Q7. How do you calculate difference between two dates?
# =====================================================

# Answer:

# start = date(2026, 8, 1)
# end = date(2026, 8, 20)
#
# difference = end - start
#
# print(difference.days)


# =====================================================
# Q8. Difference between ceil(), floor() and round()?
# =====================================================

# Answer:
#
# ceil()
# → Round upward
#
# floor()
# → Round downward
#
# round()
# → Round to nearest value


# =====================================================
# Q9. Difference between math.pow() and **?
# =====================================================

# Answer:
#
# math.pow(2, 3)
# → 8.0
#
# 2 ** 3
# → 8
#
# math.pow() converts operands to float
# and returns float.
#
# ** is Python's exponentiation operator.


# =====================================================
# Q10. Difference between randint() and randrange()?
# =====================================================

# Answer:
#
# randint(1, 10)
# → 1 through 10
#
# randrange(1, 10)
# → 1 through 9


# =====================================================
# Q11. Difference between choice(), choices()
# and sample()?
# =====================================================

# Answer:
#
# choice()
# → Select ONE item.
#
# choices()
# → Select multiple items.
# → Duplicates possible.
#
# sample()
# → Select multiple UNIQUE items.


# =====================================================
# Q12. Does shuffle() return a new list?
# =====================================================

# Answer:
# No.
#
# random.shuffle()
# modifies the original list in place
# and returns None.


# =====================================================
# Q13. Should random be used for passwords?
# =====================================================

# Answer:
# No.
#
# random is not designed for
# security-sensitive randomness.
#
# Use:
#
# secrets


# =====================================================
# Q14. random vs secrets?
# =====================================================

# Answer:
#
# random
# → simulations
# → games
# → testing
# → normal random selections
#
# secrets
# → passwords
# → security tokens
# → secure random values


# =====================================================
# Q15. Give a real-world use of datetime.
# =====================================================

# Answer:
#
# Subscription expiry
# Invoice due date
# Employee attendance
# Task deadlines
# Booking systems
# Logs
# Reports
# Scheduled jobs


# =====================================================
# Q16. How would you check whether a subscription
# has expired?
# =====================================================

# Answer:

# if date.today() > expiry_date:
#     print("Expired")


# =====================================================
# Q17. What is the output range of random.random()?
# =====================================================

# Answer:
#
# 0.0 <= value < 1.0


# =====================================================
# Q18. What does math.sqrt(64) return?
# =====================================================

# Answer:
#
# 8.0


# =====================================================
# MOST IMPORTANT INTERVIEW REVISION
# =====================================================

# 1.
# strftime() vs strptime()


# 2.
# date vs datetime


# 3.
# What is timedelta?


# 4.
# ceil() vs floor() vs round()


# 5.
# randint() vs randrange()


# 6.
# choice() vs choices() vs sample()


# 7.
# random vs secrets


# 8.
# Does shuffle() modify original list?


# 9.
# How to calculate date difference?


# 10.
# How to calculate an expiry date?


# =====================================================
# FINAL SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    "datetime → Date and Time"
)

print(
    "timedelta → Date/Time Duration"
)

print(
    "math → Mathematical Operations"
)

print(
    "random → General Random Values"
)

print(
    "secrets → Secure Random Values"
)


print("\nTopic 22 Complete")