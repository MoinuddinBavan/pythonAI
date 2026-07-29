# =====================================================
# PYTHON COLLECTION METHODS
# =====================================================

print("=" * 50)
print("Python Collection Methods")
print("=" * 50)


# =====================================================
# LIST METHODS
# =====================================================

students = ["Moin", "Aamir", "Yasin"]


# =====================================================
# 1. append()
# =====================================================

print("1. append()")

students.append("Adil")

print(students)


# =====================================================
# 2. insert()
# =====================================================

print("2. insert()")

students.insert(1, "Akib")

print(students)


# =====================================================
# 3. extend()
# =====================================================

print("3. extend()")

students.extend(["Rehan", "Imran"])

print(students)


# =====================================================
# 4. remove()
# =====================================================

print("4. remove()")

students.remove("Akib")

print(students)


# =====================================================
# 5. pop()
# =====================================================

print("5. pop()")

students.pop()

print(students)


# =====================================================
# 6. clear()
# =====================================================

print("6. clear()")

demo = [1, 2, 3]

demo.clear()

print(demo)


# =====================================================
# 7. index()
# =====================================================

print("7. index()")

print(students.index("Yasin"))


# =====================================================
# 8. count()
# =====================================================

print("8. count()")

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))


# =====================================================
# 9. sort()
# =====================================================

print("9. sort()")

numbers = [45, 12, 90, 25]

numbers.sort()

print(numbers)


# =====================================================
# 10. reverse()
# =====================================================

print("10. reverse()")

numbers.reverse()

print(numbers)


# =====================================================
# 11. copy()
# =====================================================

print("11. copy()")

new_students = students.copy()

print(new_students)


# =====================================================
# TUPLE METHODS
# =====================================================

colors = ("Red", "Blue", "Green", "Blue")


# =====================================================
# 12. tuple count()
# =====================================================

print("12. Tuple count()")

print(colors.count("Blue"))


# =====================================================
# 13. tuple index()
# =====================================================

print("13. Tuple index()")

print(colors.index("Green"))


# =====================================================
# SET METHODS
# =====================================================

skills = {"Python", "React"}


# =====================================================
# 14. add()
# =====================================================

print("14. add()")

skills.add("AI")

print(skills)


# =====================================================
# 15. update()
# =====================================================

print("15. update()")

skills.update(["Laravel", "Flutter"])

print(skills)


# =====================================================
# 16. remove()
# =====================================================

print("16. remove()")

skills.remove("React")

print(skills)


# =====================================================
# 17. discard()
# =====================================================

print("17. discard()")

skills.discard("Java")

print(skills)


# =====================================================
# 18. pop()
# =====================================================

print("18. pop()")

skills.pop()

print(skills)


# =====================================================
# 19. clear()
# =====================================================

print("19. clear()")

demo_set = {"A", "B"}

demo_set.clear()

print(demo_set)


# =====================================================
# DICTIONARY METHODS
# =====================================================

employee = {
    "name": "Moin",
    "age": 32,
    "city": "Ahmedabad"
}


# =====================================================
# 20. keys()
# =====================================================

print("20. keys()")

print(employee.keys())


# =====================================================
# 21. values()
# =====================================================

print("21. values()")

print(employee.values())


# =====================================================
# 22. items()
# =====================================================

print("22. items()")

print(employee.items())


# =====================================================
# 23. get()
# =====================================================

print("23. get()")

print(employee.get("name"))


# =====================================================
# 24. update()
# =====================================================

print("24. update()")

employee.update({"age": 33})

print(employee)


# =====================================================
# 25. pop()
# =====================================================

print("25. pop()")

employee.pop("city")

print(employee)


# =====================================================
# 26. popitem()
# =====================================================

print("26. popitem()")

employee.popitem()

print(employee)


# =====================================================
# 27. clear()
# =====================================================

print("27. clear()")

demo_dict = {"A": 1}

demo_dict.clear()

print(demo_dict)


# =====================================================
# 28. copy()
# =====================================================

print("28. copy()")

copy_employee = employee.copy()

print(copy_employee)


# =====================================================
# 29. FROMKEYS()
# =====================================================

print("29. fromkeys()")

keys = ["id", "name", "city"]

person = dict.fromkeys(keys)

print(person)


# =====================================================
# 30. setdefault()
# =====================================================

print("30. setdefault()")

employee = {"name": "Moin"}

employee.setdefault("city", "Ahmedabad")

print(employee)


# =====================================================
# 31. REAL EXAMPLE
# =====================================================

print("31. Student List")

students = ["Moin", "Aamir"]

students.append("Yasin")

students.sort()

print(students)


# =====================================================
# 32. REAL EXAMPLE
# =====================================================

print("32. Employee Record")

employee = {
    "name": "Aamir",
    "salary": 50000
}

employee.update({"department": "IT"})

print(employee)


# =====================================================
# 33. REAL EXAMPLE
# =====================================================

print("33. AI Skills")

skills = {"Python"}

skills.update(["Machine Learning", "Deep Learning"])

print(skills)


# =====================================================
# 34. REAL EXAMPLE
# =====================================================

print("34. Product")

product = {
    "name": "Laptop",
    "price": 75000
}

print(product.keys())
print(product.values())


# =====================================================
# 35. SUMMARY
# =====================================================

print("35. Summary")

# print("LIST")
# print("append()")
# print("insert()")
# print("extend()")
# print("remove()")
# print("pop()")
# print("clear()")
# print("index()")
# print("count()")
# print("sort()")
# print("reverse()")
# print("copy()")

# print()

# print("TUPLE")
# print("count()")
# print("index()")

# print()

# print("SET")
# print("add()")
# print("update()")
# print("remove()")
# print("discard()")
# print("pop()")
# print("clear()")

# print()

# print("DICTIONARY")
# print("keys()")
# print("values()")
# print("items()")
# print("get()")
# print("update()")
# print("pop()")
# print("popitem()")
# print("copy()")
# print("clear()")
# print("setdefault()")
# print("fromkeys()")

# NOTE:
#
# JavaScript Arrays  -> Python Lists
#
# push()      -> append()
# unshift()   -> insert()
# pop()       -> pop()
# shift()     -> pop(0)
# includes()  -> in
# indexOf()   -> index()
# length      -> len()
#
# Python Dictionaries are similar to
# JavaScript Objects.
#
# Python Sets automatically remove duplicates.
#
# Tuples are read-only collections.