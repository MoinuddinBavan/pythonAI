# =====================================================
# PYTHON STRINGS
# =====================================================

print("=" * 50)
print("Python Strings")
print("=" * 50)


# =====================================================
# 1. CREATE STRING
# =====================================================

print("1. Create String")

name = "Moin"
city = 'Ahmedabad'

print(name)
print(city)


# =====================================================
# 2. MULTILINE STRING
# =====================================================

print("2. Multiline String")

message = """
Welcome to
Python Programming
Course
"""

print(message)


# =====================================================
# 3. ACCESS CHARACTERS
# =====================================================

print("3. Access Characters")

language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[-1])


# =====================================================
# 4. STRING LENGTH
# =====================================================

print("4. String Length")

text = "Artificial Intelligence"

print(len(text))


# =====================================================
# 5. STRING SLICING
# =====================================================

print("5. String Slicing")

text = "Python Programming"

print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
print(text[-11:])


# =====================================================
# 6. UPPER()
# =====================================================

print("6. upper()")

name = "moin"

print(name.upper())


# =====================================================
# 7. LOWER()
# =====================================================

print("7. lower()")

name = "MOIN"

print(name.lower())


# =====================================================
# 8. TITLE()
# =====================================================

print("8. title()")

text = "python programming"

print(text.title())


# =====================================================
# 9. CAPITALIZE()
# =====================================================

print("9. capitalize()")

text = "python"

print(text.capitalize())


# =====================================================
# 10. STRIP()
# =====================================================

print("10. strip()")

text = "   Python   "

print(text.strip())


# =====================================================
# 11. REPLACE()
# =====================================================

print("11. replace()")

text = "Hello Java"

print(text.replace("Java", "Python"))


# =====================================================
# 12. SPLIT()
# =====================================================

print("12. split()")

text = "HTML,CSS,JavaScript,Python"

skills = text.split(",")

print(skills)


# =====================================================
# 13. JOIN()
# =====================================================

print("13. join()")

languages = ["Python", "JavaScript", "React"]

result = " | ".join(languages)

print(result)


# =====================================================
# 14. FIND()
# =====================================================

print("14. find()")

text = "Python Programming"

print(text.find("Programming"))
print(text.find("Java"))


# =====================================================
# 15. COUNT()
# =====================================================

print("15. count()")

text = "Python Python Java Python"

print(text.count("Python"))


# =====================================================
# 16. STARTSWITH()
# =====================================================

print("16. startswith()")

website = "https://google.com"

print(website.startswith("https"))


# =====================================================
# 17. ENDSWITH()
# =====================================================

print("17. endswith()")

filename = "photo.jpg"

print(filename.endswith(".jpg"))


# =====================================================
# 18. CHECK STRING METHODS
# =====================================================

print("18. String Checking")

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())


# =====================================================
# 19. STRING CONCATENATION
# =====================================================

print("19. String Concatenation")

first = "Moin"
last = "Bavan"

print(first + " " + last)


# =====================================================
# 20. STRING REPETITION
# =====================================================

print("20. String Repetition")

print("=" * 30)


# =====================================================
# 21. F-STRING
# =====================================================

print("21. f-string")

name = "Moin"
age = 32

print(f"My name is {name} and I am {age} years old.")


# =====================================================
# 22. REAL EXAMPLE
# =====================================================

print("22. Student Name")

student = "moin bavan"

print(student.title())


# =====================================================
# 23. REAL EXAMPLE
# =====================================================

print("23. Email Validation")

email = "moin@gmail.com"

print(email.endswith(".com"))


# =====================================================
# 24. REAL EXAMPLE
# =====================================================

print("24. AI Prompt")

prompt = "Explain Python Loops"

print(prompt.upper())


# =====================================================
# 25. REAL EXAMPLE
# =====================================================

print("25. File Name")

filename = "report.pdf"

print(filename.endswith(".pdf"))


# =====================================================
# 26. REAL EXAMPLE
# =====================================================

print("26. Search Keyword")

sentence = "Python is easy to learn."

print(sentence.find("easy"))


# =====================================================
# 27. SUMMARY
# =====================================================

print("27. Summary")

# print("len()")
# print("Slicing")
# print("upper()")
# print("lower()")
# print("title()")
# print("capitalize()")
# print("strip()")
# print("replace()")
# print("split()")
# print("join()")
# print("find()")
# print("count()")
# print("startswith()")
# print("endswith()")
# print("isalpha()")
# print("isdigit()")
# print("isalnum()")
# print("islower()")
# print("isupper()")
# print("f-string")


# NOTE:
#
# JavaScript          Python
# -----------------------------
# length          -> len()
# toUpperCase()   -> upper()
# toLowerCase()   -> lower()
# includes()      -> "in" or find()
# replace()       -> replace()
# split()         -> split()
# join()          -> join()
# trim()          -> strip()
#
# Python strings are immutable.
# Methods return a new string instead of modifying the original.