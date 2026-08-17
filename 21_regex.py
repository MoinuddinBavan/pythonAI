# =====================================================
# PYTHON REGULAR EXPRESSIONS (REGEX)
# =====================================================

print("=" * 50)
print("Python Regular Expressions")
print("=" * 50)


# =====================================================
# 1. IMPORT re
# =====================================================

print("1. Import re")

import re

# re = Regular Expression module


# =====================================================
# 2. WHAT IS REGEX?
# =====================================================

print("2. What is Regex?")

# Regex is used to:
#
# Search text
# Match patterns
# Validate data
# Extract data
# Replace text
#
# Examples:
#
# Email validation
# Phone number validation
# Password validation
# Search words
# Extract numbers


# =====================================================
# 3. re.search()
# =====================================================

print("3. re.search()")

text = "I am learning Python"

result = re.search("Python", text)

print(result)


# re.search()
# Searches anywhere in the string.


# =====================================================
# 4. CHECK SEARCH RESULT
# =====================================================

print("4. Check Search Result")

text = "Python is easy"

result = re.search("Python", text)

if result:
    print("Found")
else:
    print("Not Found")


# =====================================================
# 5. re.match()
# =====================================================

print("5. re.match()")

text = "Python Programming"

result = re.match("Python", text)

print(result)


# re.match()
# Checks from the START of the string.


# =====================================================
# 6. search() VS match()
# =====================================================

print("6. search() vs match()")

text = "I love Python"

print(re.search("Python", text))

print(re.match("Python", text))


# search()
# → Searches anywhere
#
# match()
# → Checks only from beginning


# =====================================================
# 7. re.findall()
# =====================================================

print("7. re.findall()")

text = "Python Java Python PHP Python"

result = re.findall("Python", text)

print(result)


# Output:
#
# ['Python', 'Python', 'Python']


# =====================================================
# 8. re.finditer()
# =====================================================

print("8. re.finditer()")

text = "Python Java Python"

matches = re.finditer("Python", text)

for match in matches:

    print(match.group())
    print(match.start())


# =====================================================
# 9. re.sub()
# =====================================================

print("9. re.sub()")

text = "I love PHP"

result = re.sub(
    "PHP",
    "Python",
    text
)

print(result)


# re.sub()
# Replaces matching text.


# =====================================================
# 10. re.split()
# =====================================================

print("10. re.split()")

text = "Python,Java,PHP,JavaScript"

result = re.split(",", text)

print(result)


# =====================================================
# 11. RAW STRING r""
# =====================================================

print("11. Raw String")

pattern = r"\d+"

print(pattern)


# Regex patterns are commonly written
# using raw strings:
#
# r"\d+"
#
# This avoids Python treating
# backslashes as escape characters.


# =====================================================
# 12. \d - DIGIT
# =====================================================

print("12. Digit \\d")

text = "Order number is 4587"

result = re.findall(
    r"\d",
    text
)

print(result)


# \d
# Matches one digit
#
# 0-9


# =====================================================
# 13. \d+ - ONE OR MORE DIGITS
# =====================================================

print("13. One or More Digits")

text = "Order 4587 costs 7500"

result = re.findall(
    r"\d+",
    text
)

print(result)


# Output:
#
# ['4587', '7500']


# =====================================================
# 14. \D - NON DIGIT
# =====================================================

print("14. Non Digit \\D")

text = "ABC123"

result = re.findall(
    r"\D",
    text
)

print(result)


# \D
# Matches anything except digits.


# =====================================================
# 15. \w - WORD CHARACTER
# =====================================================

print("15. Word Character \\w")

text = "AIZ_123"

result = re.findall(
    r"\w",
    text
)

print(result)


# \w matches:
#
# Letters
# Digits
# Underscore


# =====================================================
# 16. \W - NON WORD CHARACTER
# =====================================================

print("16. Non Word Character \\W")

text = "Hello @ AIZ!"

result = re.findall(
    r"\W",
    text
)

print(result)


# =====================================================
# 17. \s - WHITESPACE
# =====================================================

print("17. Whitespace \\s")

text = "Hello Python World"

result = re.findall(
    r"\s",
    text
)

print(result)


# \s matches whitespace.


# =====================================================
# 18. \S - NON WHITESPACE
# =====================================================

print("18. Non Whitespace \\S")

text = "A B C"

result = re.findall(
    r"\S",
    text
)

print(result)


# =====================================================
# 19. DOT .
# =====================================================

print("19. Dot")

text = "cat cut cot"

result = re.findall(
    r"c.t",
    text
)

print(result)


# . matches almost any single character.


# =====================================================
# 20. ^ START OF STRING
# =====================================================

print("20. Start ^")

text = "Python Programming"

result = re.search(
    r"^Python",
    text
)

print(result)


# ^ means:
#
# String must START with pattern.


# =====================================================
# 21. $ END OF STRING
# =====================================================

print("21. End $")

text = "I love Python"

result = re.search(
    r"Python$",
    text
)

print(result)


# $ means:
#
# String must END with pattern.


# =====================================================
# 22. * ZERO OR MORE
# =====================================================

print("22. Zero or More *")

text = "color colour"

result = re.findall(
    r"colou*r",
    text
)

print(result)


# * means:
#
# Previous character/pattern
# can appear zero or more times.


# =====================================================
# 23. + ONE OR MORE
# =====================================================

print("23. One or More +")

text = "123 4567 89"

result = re.findall(
    r"\d+",
    text
)

print(result)


# + means:
#
# One or more occurrences.


# =====================================================
# 24. ? ZERO OR ONE
# =====================================================

print("24. Zero or One ?")

text = "color colour"

result = re.findall(
    r"colou?r",
    text
)

print(result)


# ? means:
#
# Previous character/pattern
# is optional.


# =====================================================
# 25. {n} EXACT NUMBER
# =====================================================

print("25. Exact Number {n}")

text = "123 1234 12345"

result = re.findall(
    r"\b\d{4}\b",
    text
)

print(result)


# \d{4}
#
# Exactly 4 digits.


# =====================================================
# 26. {n,m} RANGE
# =====================================================

print("26. Range {n,m}")

text = "12 123 1234 12345"

result = re.findall(
    r"\b\d{2,4}\b",
    text
)

print(result)


# Between 2 and 4 digits.


# =====================================================
# 27. CHARACTER SET []
# =====================================================

print("27. Character Set []")

text = "cat bat mat rat"

result = re.findall(
    r"[cb]at",
    text
)

print(result)


# [cb]
#
# Match c OR b.


# =====================================================
# 28. CHARACTER RANGE
# =====================================================

print("28. Character Range")

text = "abc XYZ 123"

letters = re.findall(
    r"[a-z]",
    text
)

print(letters)


# [a-z] → lowercase letters
# [A-Z] → uppercase letters
# [0-9] → digits


# =====================================================
# 29. NEGATIVE CHARACTER SET
# =====================================================

print("29. Negative Character Set")

text = "ABC123"

result = re.findall(
    r"[^0-9]",
    text
)

print(result)


# ^ inside [] means NOT.
#
# [^0-9]
# Anything except digits.


# =====================================================
# 30. GROUP ()
# =====================================================

print("30. Group ()")

text = "Python Python Python"

result = re.findall(
    r"(Python)",
    text
)

print(result)


# () creates a group.


# =====================================================
# 31. OR |
# =====================================================

print("31. OR |")

text = "Python and Java"

result = re.findall(
    r"Python|Java",
    text
)

print(result)


# | means OR.


# =====================================================
# 32. WORD BOUNDARY \b
# =====================================================

print("32. Word Boundary")

text = "cat category cat"

result = re.findall(
    r"\bcat\b",
    text
)

print(result)


# \b matches a word boundary.
#
# This finds:
#
# cat
#
# but not:
#
# category


# =====================================================
# 33. MATCH OBJECT
# =====================================================

print("33. Match Object")

text = "Python Programming"

result = re.search(
    r"Python",
    text
)

if result:

    print(result.group())
    print(result.start())
    print(result.end())
    print(result.span())


# group()
# → Matched text
#
# start()
# → Starting position
#
# end()
# → Ending position
#
# span()
# → Start and end positions


# =====================================================
# 34. IGNORE CASE
# =====================================================

print("34. Ignore Case")

text = "python PYTHON Python"

result = re.findall(
    r"python",
    text,
    re.IGNORECASE
)

print(result)


# =====================================================
# 35. FULL MATCH
# =====================================================

print("35. re.fullmatch()")

text = "123456"

result = re.fullmatch(
    r"\d{6}",
    text
)

print(result)


# fullmatch()
#
# Entire string must match
# the pattern.


# =====================================================
# 36. VALIDATE 6-DIGIT OTP
# =====================================================

print("36. OTP Validation")

otp = "458921"

pattern = r"\d{6}"

result = re.fullmatch(
    pattern,
    otp
)

if result:

    print("Valid OTP")

else:

    print("Invalid OTP")


# =====================================================
# 37. VALIDATE INDIAN MOBILE NUMBER
# =====================================================

print("37. Mobile Validation")

mobile = "9876543210"

pattern = r"[6-9]\d{9}"

result = re.fullmatch(
    pattern,
    mobile
)

if result:

    print("Valid Mobile Number")

else:

    print("Invalid Mobile Number")


# Explanation:
#
# [6-9]
# → First digit must be 6, 7, 8 or 9
#
# \d{9}
# → Followed by exactly 9 digits


# =====================================================
# 38. SIMPLE EMAIL VALIDATION
# =====================================================

print("38. Email Validation")

email = "student@example.com"

pattern = r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}"

result = re.fullmatch(
    pattern,
    email
)

if result:

    print("Valid Email")

else:

    print("Invalid Email")


# NOTE:
#
# Real email rules are complex.
# This is a simple learning example.


# =====================================================
# 39. EXTRACT NUMBERS
# =====================================================

print("39. Extract Numbers")

text = """
Laptop price is 75000
Mouse price is 1500
Keyboard price is 3000
"""

prices = re.findall(
    r"\d+",
    text
)

print(prices)


# =====================================================
# 40. EXTRACT EMAILS
# =====================================================

print("40. Extract Emails")

text = """
Contact:
sales@example.com
support@example.org
"""

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}",
    text
)

print(emails)


# =====================================================
# 41. REMOVE EXTRA SPACES
# =====================================================

print("41. Remove Extra Spaces")

text = "Python     is    easy"

result = re.sub(
    r"\s+",
    " ",
    text
)

print(result)


# =====================================================
# 42. REAL EXAMPLE - PRODUCT CODE
# =====================================================

print("42. Product Code")

product_code = "AIZ-2026-1234"

pattern = r"AIZ-\d{4}-\d{4}"

result = re.fullmatch(
    pattern,
    product_code
)

if result:

    print("Valid Product Code")

else:

    print("Invalid Product Code")


# =====================================================
# 43. REAL EXAMPLE - USERNAME
# =====================================================

print("43. Username")

username = "moin_123"

pattern = r"[A-Za-z0-9_]{3,20}"

result = re.fullmatch(
    pattern,
    username
)

if result:

    print("Valid Username")

else:

    print("Invalid Username")


# =====================================================
# 44. REGEX QUICK REFERENCE
# =====================================================

print("44. Regex Quick Reference")

print(r"\d      -> Digit")
print(r"\D      -> Non Digit")

print(r"\w      -> Word Character")
print(r"\W      -> Non Word Character")

print(r"\s      -> Whitespace")
print(r"\S      -> Non Whitespace")

print(".       -> Any Character")

print("^       -> Start")
print("$       -> End")

print("*       -> Zero or More")
print("+       -> One or More")
print("?       -> Zero or One")

print("{n}     -> Exactly n")
print("{n,m}   -> Between n and m")

print("[]      -> Character Set")
print("[^]     -> Not in Character Set")

print("()      -> Group")
print("|       -> OR")

print(r"\b      -> Word Boundary")


# =====================================================
# 45. IMPORTANT re METHODS
# =====================================================

print("45. Important re Methods")

print("re.search()")
print("re.match()")
print("re.fullmatch()")
print("re.findall()")
print("re.finditer()")
print("re.sub()")
print("re.split()")


# =====================================================
# 46. SUMMARY
# =====================================================

print("46. Summary")

print("Regex = Pattern Matching")

print("re.search() = Search Anywhere")

print("re.match() = Match From Start")

print("re.fullmatch() = Match Entire String")

print("re.findall() = Find All Matches")

print("re.finditer() = Iterate Matches")

print("re.sub() = Replace")

print("re.split() = Split")

print(r"\d = Digit")

print(r"\w = Word Character")

print(r"\s = Whitespace")

print("^ = Start")

print("$ = End")

print("+ = One or More")

print("* = Zero or More")

print("? = Optional")