# =====================================================
# PYTHON CSV & JSON
# =====================================================

print("=" * 50)
print("Python CSV & JSON")
print("=" * 50)


# =====================================================
# 1. IMPORT CSV
# =====================================================

print("1. Import CSV")

import csv


# =====================================================
# 2. WRITE CSV
# =====================================================

print("2. Write CSV")

# with open("students.csv", "w", newline="") as file:
#
#     writer = csv.writer(file)
#
#     writer.writerow(["Name", "Marks"])
#     writer.writerow(["Moin", 90])
#     writer.writerow(["Aamir", 85])


# =====================================================
# 3. READ CSV
# =====================================================

print("3. Read CSV")

# with open("students.csv", "r") as file:
#
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)


# =====================================================
# 4. DICTIONARY WRITER
# =====================================================

print("4. DictWriter")

# with open("employees.csv", "w", newline="") as file:
#
#     fields = ["Name", "Salary"]
#
#     writer = csv.DictWriter(file, fieldnames=fields)
#
#     writer.writeheader()
#
#     writer.writerow({"Name":"Moin","Salary":50000})
#     writer.writerow({"Name":"Aamir","Salary":60000})


# =====================================================
# 5. DICTIONARY READER
# =====================================================

print("5. DictReader")

# with open("employees.csv", "r") as file:
#
#     reader = csv.DictReader(file)
#
#     for row in reader:
#
#         print(row["Name"], row["Salary"])


# =====================================================
# 6. IMPORT JSON
# =====================================================

print("6. Import JSON")

import json


# =====================================================
# 7. PYTHON TO JSON
# =====================================================

print("7. Python to JSON")

student = {
    "name": "Moin",
    "marks": 90,
    "city": "Ahmedabad"
}

json_data = json.dumps(student)

print(json_data)


# =====================================================
# 8. JSON TO PYTHON
# =====================================================

print("8. JSON to Python")

data = '{"name":"Aamir","marks":85}'

python_data = json.loads(data)

print(python_data)

print(type(python_data))


# =====================================================
# 9. WRITE JSON FILE
# =====================================================

print("9. Write JSON")

# employee = {
#     "name":"Moin",
#     "salary":50000
# }
#
# with open("employee.json","w") as file:
#
#     json.dump(employee,file,indent=4)


# =====================================================
# 10. READ JSON FILE
# =====================================================

print("10. Read JSON")

# with open("employee.json","r") as file:
#
#     data = json.load(file)
#
#     print(data)


# =====================================================
# 11. JSON INDENT
# =====================================================

print("11. JSON Indent")

print(json.dumps(student, indent=4))


# =====================================================
# 12. JSON SORT KEYS
# =====================================================

print("12. Sort Keys")

print(json.dumps(student, indent=4, sort_keys=True))


# =====================================================
# 13. REAL EXAMPLE
# =====================================================

print("13. Student Data")

students = [
    {
        "name":"Moin",
        "marks":90
    },
    {
        "name":"Aamir",
        "marks":82
    }
]

print(json.dumps(students, indent=4))


# =====================================================
# 14. REAL EXAMPLE
# =====================================================

print("14. Product")

product = {
    "name":"Laptop",
    "price":75000,
    "stock":15
}

print(json.dumps(product, indent=4))


# =====================================================
# 15. REAL EXAMPLE
# =====================================================

print("15. API Response")

response = {
    "success":True,
    "message":"Login Successful",
    "user":{
        "id":1,
        "name":"Moin"
    }
}

print(json.dumps(response, indent=4))


# =====================================================
# 16. REAL EXAMPLE
# =====================================================

print("16. AI Prompt")

prompt = {
    "model":"gpt-5",
    "temperature":0.7,
    "prompt":"Explain Python"
}

print(json.dumps(prompt, indent=4))


# =====================================================
# 17. SUMMARY
# =====================================================

print("17. Summary")

print("csv.writer()")
print("csv.reader()")
print("DictWriter")
print("DictReader")
print("json.dumps()")
print("json.loads()")
print("json.dump()")
print("json.load()")
print("indent")
print("sort_keys")


# NOTE:
#
# CSV
# ----
# Stores data in rows and columns.
#
# Used in:
# ✔ Excel
# ✔ Reports
# ✔ Machine Learning Datasets
#
#
# JSON
# -----
# Stores data as key-value pairs.
#
# Used in:
# ✔ REST APIs
# ✔ FastAPI
# ✔ Django
# ✔ React
# ✔ AI Models
# ✔ ChatGPT APIs
#
#
# Remember:
#
# dumps()  -> Python Object → JSON String
#
# loads()  -> JSON String → Python Object
#
#
# dump()   -> Write JSON File
#
# load()   -> Read JSON File