# =====================================================
# PYTHON MODULES & PACKAGES
# =====================================================

print("=" * 50)
print("Python Modules & Packages")
print("=" * 50)


# =====================================================
# 1. IMPORT MODULE # Module = a Python file/toolbox containing ready-made code that we can reuse.
# =====================================================

print("1. Import Module")

import math

print(math.sqrt(25))
print(math.factorial(5))




# =====================================================
# 2. IMPORT SPECIFIC FUNCTION
# =====================================================

print("2. Import Specific Function")

from math import sqrt

print(sqrt(81))


# =====================================================
# 3. IMPORT MULTIPLE FUNCTIONS
# =====================================================

print("3. Import Multiple Functions")

from math import sqrt, factorial

print(sqrt(100))
print(factorial(6))


# =====================================================
# 4. IMPORT WITH ALIAS
# =====================================================

print("4. Import with Alias")

import math as m

print(m.pi)
print(m.pow(2, 5))


# =====================================================
# 5. MODULE INFORMATION
# =====================================================

print("5. Module Information")

import math

print(dir(math))


# =====================================================
# 6. RANDOM MODULE
# =====================================================

print("6. Random Module")

import random

print(random.randint(1, 100))
print(random.choice(["Python", "React", "AI"]))


# =====================================================
# 7. DATETIME MODULE
# =====================================================

print("7. Datetime Module")

import datetime

today = datetime.datetime.now()

print(today)


# =====================================================
# 8. OS MODULE
# =====================================================

print("8. OS Module")

import os

print(os.getcwd())


# =====================================================
# 9. SYS MODULE # Provides access to some variables used or maintained by the Python interpreter.
# =====================================================

print("9. Sys Module")

import sys

print(sys.version)


# =====================================================
# 10. PLATFORM MODULE
# =====================================================

print("10. Platform Module")

import platform

print(platform.system())
print(platform.machine())



# =====================================================
# 13. PACKAGE
# =====================================================

print("13. Package")

print("""
project/

    calculator/

        __init__.py

        math.py

        tax.py

        discount.py
""")


# =====================================================
# 14. FROM PACKAGE IMPORT
# =====================================================

print("14. From Package Import")

print("""
from calculator.math import add
""")




# =====================================================
# 19. REAL EXAMPLE
# =====================================================

print("19. Random OTP")

import random

otp = random.randint(100000, 999999)

print("OTP :", otp)


# =====================================================
# 20. REAL EXAMPLE
# =====================================================

print("20. Current Date")

import datetime

print(datetime.date.today())


# =====================================================
# 21. REAL EXAMPLE
# =====================================================

print("21. AI Project")

import math

tokens = 500

print(math.ceil(tokens / 128))


# =====================================================
# 22. REAL EXAMPLE
# =====================================================

print("22. Project Folder")

print("""
AI_Project/

    main.py

    config.py

    database.py

    utils.py

    models.py

    api.py
""")


# =====================================================
# 23. SUMMARY
# =====================================================

print("23. Summary")

print("import")
print("from import")
print("Alias")
print("math")
print("random")
print("datetime")
print("os")
print("sys")
print("platform")