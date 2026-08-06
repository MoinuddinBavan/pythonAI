# =====================================================
# PYTHON FILE HANDLING
# =====================================================

print("=" * 50)
print("Python File Handling")
print("=" * 50)


# =====================================================
# 1. OPEN FILE (READ MODE)
# =====================================================

print("1. Open File")

# file = open("data.txt", "r")
# print(file.read())
# file.close()


# =====================================================
# 2. READ FILE
# =====================================================

print("2. Read File")

# file = open("data.txt", "r")
# print(file.read())
# file.close()


# =====================================================
# 3. READ ONE LINE
# =====================================================

print("3. Read One Line")

# file = open("data.txt", "r")
# print(file.readline())
# file.close()


# =====================================================
# 4. READ ALL LINES
# =====================================================

print("4. Read All Lines")

# file = open("data.txt", "r")
# print(file.readlines())
# file.close()


# =====================================================
# 5. LOOP THROUGH FILE
# =====================================================

print("5. Loop Through File")

# file = open("data.txt", "r")
#
# for line in file:
#     print(line.strip())
#
# file.close()


# =====================================================
# 6. WRITE FILE
# =====================================================

print("6. Write File")

# file = open("demo.txt", "w")
# file.write("Hello Python")
# file.close()


# =====================================================
# 7. APPEND FILE
# =====================================================

print("7. Append File")

# file = open("demo.txt", "a")
# file.write("\nWelcome")
# file.close()


# =====================================================
# 8. WITH OPEN()
# =====================================================

print("8. with open()")

# with open("data.txt", "r") as file:
#
#     print(file.read())

# Automatically closes the file.


# =====================================================
# 9. CHECK FILE EXISTS
# =====================================================

print("9. File Exists")

import os

print(os.path.exists("data.txt"))


# =====================================================
# 10. DELETE FILE
# =====================================================

print("10. Delete File")

# import os
#
# os.remove("demo.txt")


# =====================================================
# 11. FILE MODES
# =====================================================

print("11. File Modes")

print("r  -> Read")
print("w  -> Write")
print("a  -> Append")
print("x  -> Create")
print("rb -> Read Binary")
print("wb -> Write Binary")


# =====================================================
# 12. CREATE FILE
# =====================================================

print("12. Create File")

# file = open("new.txt", "x")
# file.close()


# =====================================================
# 13. REAL EXAMPLE
# =====================================================

print("13. Student Report")

student = "Moin"

marks = 91

# with open("student.txt", "w") as file:
#
#     file.write(student)
#     file.write("\n")
#     file.write(str(marks))


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Employee Log")

# with open("employees.txt", "a") as file:
#
#     file.write("Aamir - 50000\n")


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. AI Prompt")

prompt = "Explain Machine Learning"

# with open("prompt.txt", "w") as file:
#
#     file.write(prompt)


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. Application Log")

# with open("log.txt", "a") as file:
#
#     file.write("Application Started\n")


# =====================================================
# 17. SUMMARY
# =====================================================

print("17. Summary")

print("open()")
print("read()")
print("readline()")
print("readlines()")
print("write()")
print("append()")
print("close()")
print("with open()")
print("File Modes")
print("os.path.exists()")
print("os.remove()")