# =====================================================
# PYTHON FILE HANDLING
# =====================================================

print("=" * 50)
print("Python File Handling")
print("=" * 50)


# =====================================================
# 1. OPEN FILE (READ MODE)
# =====================================================

print("\n1. Open File (Read Mode)")

# "r" means Read Mode.
# The file must already exist.

with open("data.txt", "r") as file:
    print(file.read())


# =====================================================
# 2. READ FILE
# =====================================================

print("\n2. read()")

# read() reads the complete file.

with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# =====================================================
# 3. READ ONE LINE
# =====================================================

print("\n3. readline()")

# readline() reads one line at a time.

with open("data.txt", "r") as file:
    print(file.readline())


# =====================================================
# 4. READ ALL LINES
# =====================================================

print("\n4. readlines()")

# readlines() returns all lines as a list.

with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)


# =====================================================
# 5. LOOP THROUGH FILE
# =====================================================

print("\n5. Loop Through File")

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# =====================================================
# 6. WRITE FILE
# =====================================================

print("\n6. Write File")

# "w" means Write Mode.
# Creates the file if it does not exist.
# WARNING: Existing content is overwritten.

with open("demo.txt", "w") as file:
    file.write("Hello Python")

print("Data written to demo.txt")


# =====================================================
# 7. APPEND FILE
# =====================================================

print("\n7. Append File")

# "a" means Append Mode.
# Adds new content without deleting old content.

with open("demo.txt", "a") as file:
    file.write("\nWelcome to File Handling")

print("Data appended to demo.txt")


# =====================================================
# 8. WITH OPEN()
# =====================================================

print("\n8. with open()")

# with open() automatically closes the file.

with open("data.txt", "r") as file:
    print(file.read())


# =====================================================
# 9. CHECK FILE EXISTS
# =====================================================

print("\n9. Check File Exists")

import os

print(os.path.exists("data.txt"))


# =====================================================
# 10. DELETE FILE
# =====================================================

print("\n10. Delete File")

# Use os.remove() to delete a file.
# Kept commented so the file is not deleted accidentally.

# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("demo.txt deleted")


# =====================================================
# 11. FILE MODES
# =====================================================

print("\n11. File Modes")

print("r  -> Read")
print("w  -> Write / Overwrite")
print("a  -> Append")
print("x  -> Create")
print("rb -> Read Binary")
print("wb -> Write Binary")


# =====================================================
# 12. CREATE FILE
# =====================================================

print("\n12. Create File")

# "x" creates a new file.
# It gives an error if the file already exists.

# with open("new.txt", "x") as file:
#     pass


# =====================================================
# 13. STUDENT REPORT EXAMPLE
# =====================================================

print("\n13. Student Report")

student = "Moin"
marks = 91

with open("student.txt", "w") as file:
    file.write(student)
    file.write("\n")
    file.write(str(marks))

print("Student report created")


# =====================================================
# 14. EMPLOYEE LOG EXAMPLE
# =====================================================

print("\n14. Employee Log")

with open("employees.txt", "a") as file:
    file.write("Aamir - 50000\n")

print("Employee added to log")


# =====================================================
# 15. AI PROMPT EXAMPLE
# =====================================================

print("\n15. AI Prompt")

prompt = "Explain Machine Learning"

with open("prompt.txt", "w") as file:
    file.write(prompt)

print("Prompt saved")


# =====================================================
# 16. APPLICATION LOG EXAMPLE
# =====================================================

print("\n16. Application Log")

with open("log.txt", "a") as file:
    file.write("Application Started\n")

print("Application log updated")


# =====================================================
# 17. SUMMARY
# =====================================================

print("\n17. Summary")

print("""
open()          -> Open a file
read()          -> Read complete file
readline()      -> Read one line
readlines()     -> Read all lines into a list
write()         -> Write data
close()         -> Close file
with open()     -> Automatically closes file

r  -> Read
w  -> Write / Overwrite
a  -> Append
x  -> Create

os.path.exists() -> Check whether file exists
os.remove()      -> Delete file
""")
