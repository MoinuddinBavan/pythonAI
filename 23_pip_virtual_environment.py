# =====================================================
# 23. PIP AND VIRTUAL ENVIRONMENT
# =====================================================

print("=" * 60)
print("Python - pip and Virtual Environment")
print("=" * 60)


# =====================================================
# IMPORTANT:
# =====================================================

# Most commands in this topic are TERMINAL commands.
#
# They are NOT Python code.
#
# So commands like:
#
# pip install requests
#
# should be written inside:
#
# VS Code Terminal
# Command Prompt
# PowerShell
#
# NOT directly inside Python code.


# =====================================================
# PART 1 - WHAT IS pip?
# =====================================================

print("\n" + "=" * 60)
print("PART 1 - PIP")
print("=" * 60)


# =====================================================
# 1. WHAT IS pip?
# =====================================================

print("\n1. What is pip?")

# pip is Python's package installer.
#
# It is used to install external Python packages.


# Example:
#
# Python already contains built-in modules:
#
# math
# random
# datetime
# os
#
#
# But some libraries are NOT built into Python.
#
# Examples:
#
# requests
# numpy
# pandas
# fastapi
# sqlalchemy
# pytest
#
#
# To install them:
#
# pip install package_name


# Easy:
#
# pip
# ↓
# Download and install Python packages


# =====================================================
# 2. BUILT-IN MODULE VS EXTERNAL PACKAGE
# =====================================================

print("\n2. Built-in vs External Package")


# BUILT-IN
#
# Already comes with Python.
#
# Example:

import math
import random


# We DON'T need:
#
# pip install math
#
# ❌


# EXTERNAL PACKAGE
#
# Must normally be installed separately.
#
# Example:
#
# requests
# pandas
# fastapi


# =====================================================
# 3. CHECK pip VERSION
# =====================================================

print("\n3. Check pip Version")


# TERMINAL:
#
# pip --version


# Better / safer command:
#
# python -m pip --version


# Example output:
#
# pip 26.x from ...
#
#
# This tells us:
#
# pip version
# installation location
# Python environment being used


# =====================================================
# IMPORTANT NEW SYNTAX
# python -m pip
# =====================================================

# You will often see:
#
# python -m pip install requests


# What is:
#
# -m
#
# ?
#
# -m means:
#
# "Run this Python module"


# So:
#
# python -m pip
#
# means:
#
# Use this Python interpreter
#      ↓
# Run its pip module


# This is often safer than only:
#
# pip
#
# because it helps ensure pip belongs to
# the Python interpreter you are using.


# =====================================================
# 4. INSTALL A PACKAGE
# =====================================================

print("\n4. Install Package")


# TERMINAL:
#
# python -m pip install requests


# Flow:
#
# PyPI
#   ↓
# Find requests package
#   ↓
# Download package
#   ↓
# Install package
#   ↓
# We can import requests


# After installation:
#
# import requests


# =====================================================
# 5. WHAT IS PyPI?
# =====================================================

print("\n5. PyPI")


# PyPI
# ↓
# Python Package Index
#
# It is a large repository of Python packages.
#
#
# Examples:
#
# requests
# numpy
# pandas
# fastapi
# django
# pytest
#
#
# pip normally downloads packages from PyPI.


# Easy:
#
# PyPI
# ↓
# Python package store/repository
#
# pip
# ↓
# Package installer


# =====================================================
# 6. INSTALL SPECIFIC VERSION
# =====================================================

print("\n6. Install Specific Version")


# TERMINAL:
#
# python -m pip install requests==2.32.5


# == means:
#
# Install EXACTLY this version.


# Example:
#
# requests==2.32.5
#
# Package:
# requests
#
# Version:
# 2.32.5


# =====================================================
# 7. UPGRADE A PACKAGE
# =====================================================

print("\n7. Upgrade Package")


# TERMINAL:
#
# python -m pip install --upgrade requests


# --upgrade
# ↓
# Update package to a newer compatible/latest
# available version requested by pip.


# Short form:
#
# python -m pip install -U requests


# =====================================================
# 8. UNINSTALL A PACKAGE
# =====================================================

print("\n8. Uninstall Package")


# TERMINAL:
#
# python -m pip uninstall requests


# pip will ask:
#
# Proceed (Y/n)?
#
# Enter:
#
# y


# =====================================================
# 9. LIST INSTALLED PACKAGES
# =====================================================

print("\n9. List Packages")


# TERMINAL:
#
# python -m pip list


# Example:
#
# Package       Version
# ------------  -------
# pip           26.x
# requests      2.x
# urllib3       2.x


# =====================================================
# 10. SHOW PACKAGE DETAILS
# =====================================================

print("\n10. Package Details")


# TERMINAL:
#
# python -m pip show requests


# It can show:
#
# Name
# Version
# Summary
# Location
# Dependencies


# =====================================================
# 11. CHECK PACKAGE DEPENDENCY PROBLEMS
# =====================================================

print("\n11. pip check")


# TERMINAL:
#
# python -m pip check


# pip check
# ↓
# Checks whether installed packages
# have broken/incompatible dependencies.


# =====================================================
# PART 2 - PACKAGE DEPENDENCIES
# =====================================================

print("\n" + "=" * 60)
print("PART 2 - DEPENDENCIES")
print("=" * 60)


# =====================================================
# 12. WHAT IS A DEPENDENCY?
# =====================================================

print("\n12. What is a Dependency?")


# Suppose our application uses:
#
# FastAPI
#
# FastAPI itself may depend on
# other packages.


# Think:
#
# OUR PROJECT
#     ↓
# FastAPI
#     ↓
# Other required packages


# A dependency is:
#
# A package/library that another
# project or package needs to work.


# Real example:
#
# Our project needs:
#
# requests
# fastapi
# sqlalchemy
#
# These are project dependencies.


# =====================================================
# PART 3 - requirements.txt
# =====================================================

print("\n" + "=" * 60)
print("PART 3 - requirements.txt")
print("=" * 60)


# =====================================================
# 13. WHAT IS requirements.txt?
# =====================================================

print("\n13. requirements.txt")


# requirements.txt is a text file
# containing project dependencies.


# Example contents:
#
# fastapi==0.x.x
# requests==2.x.x
# sqlalchemy==2.x.x


# It allows another developer/server to install
# project packages easily.


# =====================================================
# 14. CREATE requirements.txt
# =====================================================

print("\n14. Create requirements.txt")


# TERMINAL:
#
# python -m pip freeze > requirements.txt


# IMPORTANT NEW SYMBOL:
#
# >
#
# This is TERMINAL redirection.
#
# It means:
#
# Take output from left command
#        ↓
# Save it into file on right


# Example:
#
# pip freeze
#     ↓
# Shows installed packages
#
#
# pip freeze > requirements.txt
#     ↓
# Saves installed package versions
# into requirements.txt


# =====================================================
# 15. pip freeze
# =====================================================

print("\n15. pip freeze")


# TERMINAL:
#
# python -m pip freeze


# Example output:
#
# requests==2.32.5
# urllib3==2.x.x
# certifi==2026.x.x


# Difference:
#
# pip list
# ↓
# Human-friendly package list
#
#
# pip freeze
# ↓
# requirements-style output
# normally used for dependency files


# =====================================================
# 16. INSTALL FROM requirements.txt
# =====================================================

print("\n16. Install Requirements")


# TERMINAL:
#
# python -m pip install -r requirements.txt


# IMPORTANT:
#
# -r
# ↓
# Read dependencies from a requirements file.


# Flow:
#
# requirements.txt
#       ↓
# pip install -r
#       ↓
# Install all packages
#       ↓
# Project dependencies ready


# =====================================================
# REAL PROJECT EXAMPLE
# =====================================================

# Developer A creates project:
#
# project/
# │
# ├── main.py
# └── requirements.txt
#
#
# requirements.txt:
#
# fastapi==...
# sqlalchemy==...
# requests==...


# Developer B downloads project.
#
# Developer B runs:
#
# python -m pip install -r requirements.txt
#
#
# All required dependencies are installed.


# =====================================================
# PART 4 - VIRTUAL ENVIRONMENT
# =====================================================

print("\n" + "=" * 60)
print("PART 4 - VIRTUAL ENVIRONMENT")
print("=" * 60)


# =====================================================
# 17. WHAT IS A VIRTUAL ENVIRONMENT?
# =====================================================

print("\n17. Virtual Environment")


# Virtual Environment
#
# creates an isolated Python environment
# for ONE project.


# Easy example:
#
#
# COMPUTER
# │
# ├── Project A
# │     └── Its own packages
# │
# ├── Project B
# │     └── Its own packages
# │
# └── Project C
#       └── Its own packages


# Each project can have its own:
#
# packages
# package versions
# dependencies


# =====================================================
# 18. WHY DO WE NEED VIRTUAL ENVIRONMENT?
# =====================================================

print("\n18. Why Virtual Environment?")


# Imagine:
#
# PROJECT A
#
# needs:
#
# package version 1
#
#
# PROJECT B
#
# needs:
#
# package version 2
#
#
# Without isolated environments:
#
# VERSION CONFLICT ❌


# With virtual environments:
#
# Project A
# └── package v1
#
# Project B
# └── package v2
#
# No conflict ✅


# =====================================================
# 19. REAL FASTAPI EXAMPLE
# =====================================================

print("\n19. Real Project Example")


# CRM PROJECT
#
# .venv/
#   ↓
# fastapi
# sqlalchemy
# psycopg
# pydantic
#
#
# AI PROJECT
#
# .venv/
#   ↓
# numpy
# pandas
# torch
# transformers
#
#
# Packages remain isolated by project.


# =====================================================
# 20. venv MODULE
# =====================================================

print("\n20. venv")


# Python includes a built-in module:
#
# venv


# We use it to create virtual environments.


# TERMINAL:
#
# python -m venv .venv


# Breakdown:
#
# python
# ↓
# Run Python
#
#
# -m
# ↓
# Run a module
#
#
# venv
# ↓
# Virtual environment module
#
#
# .venv
# ↓
# Name/folder for our environment


# =====================================================
# 21. WHY .venv?
# =====================================================

print("\n21. Why .venv?")


# You may see names such as:
#
# venv
# env
# .venv


# We will use:
#
# .venv


# The leading dot commonly indicates
# a project/tool folder that should not
# be treated as normal source code.


# Example:
#
# my_project/
# │
# ├── .venv/
# ├── main.py
# └── requirements.txt


# =====================================================
# 22. CREATE VIRTUAL ENVIRONMENT
# =====================================================

print("\n22. Create Virtual Environment")


# First open terminal in project folder.


# TERMINAL:
#
# python -m venv .venv


# After running:
#
# project/
# │
# ├── .venv/
# │
# └── main.py


# =====================================================
# 23. ACTIVATE VIRTUAL ENVIRONMENT - WINDOWS
# =====================================================

print("\n23. Activate on Windows")


# WINDOWS POWERSHELL:
#
# .\.venv\Scripts\Activate.ps1


# WINDOWS COMMAND PROMPT:
#
# .venv\Scripts\activate.bat


# Sometimes this also works depending
# on the terminal:
#
# .venv\Scripts\activate


# After activation you may see:
#
# (.venv)
#
# before your terminal path.


# Example:
#
# (.venv) C:\project>


# That means:
#
# Virtual environment is ACTIVE ✅


# =====================================================
# 24. ACTIVATE ON macOS / LINUX
# =====================================================

print("\n24. Activate on macOS / Linux")


# TERMINAL:
#
# source .venv/bin/activate


# =====================================================
# 25. DEACTIVATE VIRTUAL ENVIRONMENT
# =====================================================

print("\n25. Deactivate")


# TERMINAL:
#
# deactivate


# Then:
#
# (.venv)
#
# disappears.


# =====================================================
# 26. IMPORTANT WORKFLOW
# =====================================================

print("\n26. Virtual Environment Workflow")


# STEP 1
#
# Create project folder


# STEP 2
#
# Open project folder in VS Code


# STEP 3
#
# Create virtual environment:
#
# python -m venv .venv


# STEP 4
#
# Activate:
#
# Windows PowerShell:
#
# .\.venv\Scripts\Activate.ps1


# STEP 5
#
# Install package:
#
# python -m pip install requests


# STEP 6
#
# Save dependencies:
#
# python -m pip freeze > requirements.txt


# STEP 7
#
# Work on project


# STEP 8
#
# When finished:
#
# deactivate


# =====================================================
# VISUAL FLOW
# =====================================================

# PROJECT
#    ↓
# Create .venv
#    ↓
# Activate .venv
#    ↓
# Install Packages
#    ↓
# Develop Project
#    ↓
# requirements.txt
#    ↓
# Deactivate


# =====================================================
# PART 5 - CHECK WHICH PYTHON IS RUNNING
# =====================================================

print("\n" + "=" * 60)
print("PART 5 - CHECK ENVIRONMENT")
print("=" * 60)


# =====================================================
# 27. sys.executable
# =====================================================

print("\n27. Python Executable")


# NEW MODULE:
#
# sys
#
# sys provides information and functionality
# related to the Python interpreter/runtime.


import sys


print(
    "Python Executable:"
)

print(
    sys.executable
)


# Outside virtual environment:
#
# Could show something like:
#
# C:\Python\python.exe


# Inside virtual environment:
#
# Could show:
#
# C:\project\.venv\Scripts\python.exe


# This helps prove which Python interpreter
# VS Code / terminal is using.


# =====================================================
# 28. CHECK PYTHON VERSION
# =====================================================

print("\n28. Python Version")

print(
    sys.version
)


# =====================================================
# 29. CHECK WHETHER VENV IS ACTIVE
# =====================================================

print("\n29. Check Virtual Environment")


is_virtual_environment = (
    sys.prefix != sys.base_prefix
)


print(
    "Virtual Environment Active:",
    is_virtual_environment
)


# NEW CONCEPT:
#
# sys.prefix
# ↓
# Current Python environment location
#
#
# sys.base_prefix
# ↓
# Base Python installation location


# If:
#
# sys.prefix != sys.base_prefix
#
# usually means:
#
# Virtual environment is active.


# Example:
#
# True
# ↓
# Virtual environment active
#
#
# False
# ↓
# Using base/global Python


# =====================================================
# PART 6 - GLOBAL VS VIRTUAL INSTALLATION
# =====================================================

print("\n" + "=" * 60)
print("PART 6 - GLOBAL VS VIRTUAL")
print("=" * 60)


# =====================================================
# 30. GLOBAL INSTALLATION
# =====================================================

print("\n30. Global Installation")


# If no virtual environment is active
# and you run:
#
# pip install requests
#
# it may install into your user/global
# Python environment depending on setup.


# Then multiple projects may use it.


# =====================================================
# 31. VIRTUAL INSTALLATION
# =====================================================

print("\n31. Virtual Installation")


# Activate:
#
# .venv
#
# Then:
#
# python -m pip install requests
#
#
# It installs into:
#
# THIS PROJECT'S virtual environment


# Think:
#
# GLOBAL PYTHON
# ├── Shared packages
#
#
# PROJECT A .venv
# ├── Its packages
#
#
# PROJECT B .venv
# ├── Its packages


# =====================================================
# BEST PRACTICE
# =====================================================

# For real projects:
#
# ✅ Create virtual environment
# ✅ Activate it
# ✅ Install dependencies inside it
# ✅ Save requirements
#
#
# Avoid installing every project package
# globally.


# =====================================================
# PART 7 - VS CODE PYTHON INTERPRETER
# =====================================================

print("\n" + "=" * 60)
print("PART 7 - VS CODE INTERPRETER")
print("=" * 60)


# =====================================================
# 32. SELECT INTERPRETER
# =====================================================

print("\n32. Select Python Interpreter")


# After creating .venv,
# VS Code often detects it automatically.


# If not:
#
# Press:
#
# Ctrl + Shift + P
#
#
# Search:
#
# Python: Select Interpreter
#
#
# Choose:
#
# .venv


# Example:
#
# .venv\Scripts\python.exe


# This is important because:
#
# VS Code
#     ↓
# should run
#     ↓
# Project's Python
#     ↓
# Project's installed packages


# =====================================================
# PART 8 - .gitignore
# =====================================================

print("\n" + "=" * 60)
print("PART 8 - .gitignore")
print("=" * 60)


# =====================================================
# 33. SHOULD .venv GO TO GITHUB?
# =====================================================

print("\n33. Should .venv be uploaded?")


# Normally:
#
# NO ❌


# We normally do NOT upload:
#
# .venv/
#
# to GitHub.


# Instead upload:
#
# requirements.txt


# Why?
#
# .venv can contain:
#
# thousands of files
# OS-specific files
# installed packages
#
#
# Another developer can recreate it using:
#
# requirements.txt


# =====================================================
# 34. .gitignore
# =====================================================

print("\n34. .gitignore")


# Add this inside .gitignore:
#
# .venv/


# Example:
#
# .gitignore
#
# ---------------------
# .venv/
# __pycache__/
# .env
# ---------------------


# =====================================================
# PART 9 - .env BASICS
# =====================================================

print("\n" + "=" * 60)
print("PART 9 - .env BASICS")
print("=" * 60)


# NOTE:
#
# Detailed environment configuration will be used
# later with FastAPI and production projects.
#
# For now understand the basic idea.


# =====================================================
# 35. WHAT IS .env?
# =====================================================

print("\n35. What is .env?")


# .env is commonly used to keep
# configuration values separate from code.


# Example:
#
# .env
#
# DATABASE_URL=postgresql://...
# API_KEY=...
# SECRET_KEY=...


# We should NOT write sensitive values directly
# inside source code like:
#
# API_KEY = "my-secret-key"
#
# ❌


# Better:
#
# Store configuration separately.
#
# .env
# ↓
# Application reads it


# =====================================================
# 36. IMPORTANT SECURITY RULE
# =====================================================

print("\n36. .env Security")


# Normally add:
#
# .env
#
# to:
#
# .gitignore


# Example:
#
# .gitignore
#
# .venv/
# .env


# Never intentionally commit real passwords,
# API keys or production secrets to Git.


# =====================================================
# 37. python-dotenv
# =====================================================

print("\n37. python-dotenv")


# A commonly used package is:
#
# python-dotenv


# TERMINAL:
#
# python -m pip install python-dotenv


# Example .env file:
#
# APP_NAME=AIZ AI Application
# DEBUG=True


# Python example:
#
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# app_name = os.getenv("APP_NAME")
#
# print(app_name)


# IMPORTANT:
#
# dotenv loading belongs more deeply to
# application configuration.
#
# We will use it again in FastAPI.


# =====================================================
# PART 10 - REAL PROJECT SETUP
# =====================================================

print("\n" + "=" * 60)
print("PART 10 - REAL PROJECT SETUP")
print("=" * 60)


# =====================================================
# 38. COMPLETE NEW PROJECT WORKFLOW
# =====================================================

print("\n38. Complete Workflow")


# Imagine we create:
#
# customer_api/


# STEP 1
#
# Open folder:
#
# customer_api


# STEP 2
#
# Create virtual environment:
#
# python -m venv .venv


# STEP 3
#
# Activate:
#
# Windows PowerShell:
#
# .\.venv\Scripts\Activate.ps1


# STEP 4
#
# Upgrade pip if required:
#
# python -m pip install --upgrade pip


# STEP 5
#
# Install packages:
#
# python -m pip install requests


# STEP 6
#
# Check:
#
# python -m pip list


# STEP 7
#
# Save:
#
# python -m pip freeze > requirements.txt


# Project might now look like:
#
# customer_api/
# │
# ├── .venv/
# ├── main.py
# ├── requirements.txt
# └── .gitignore


# .gitignore:
#
# .venv/
# .env
# __pycache__/


# =====================================================
# 39. ANOTHER DEVELOPER SETUP
# =====================================================

print("\n39. Setup Existing Project")


# Suppose another developer downloads:
#
# customer_api/
#
# ├── main.py
# ├── requirements.txt
# └── .gitignore


# They DO NOT need your .venv folder.


# They run:


# STEP 1:
#
# python -m venv .venv


# STEP 2:
#
# Activate .venv


# STEP 3:
#
# python -m pip install -r requirements.txt


# Done ✅


# =====================================================
# 40. WHY THIS MATTERS FOR AI/ML
# =====================================================

print("\n40. Why Important for AI/ML?")


# Later we may have:


# MACHINE LEARNING PROJECT
#
# .venv
# ├── numpy
# ├── pandas
# ├── scikit-learn
# └── matplotlib


# LLM PROJECT
#
# .venv
# ├── transformers
# ├── torch
# ├── fastapi
# └── other AI libraries


# Different projects can require
# different versions.


# Therefore:
#
# Virtual environments are VERY important
# in Python / AI development.


# =====================================================
# QUICK REVISION
# =====================================================

print("\n" + "=" * 60)
print("QUICK REVISION")
print("=" * 60)


# pip
# ↓
# Install/manage Python packages


# PyPI
# ↓
# Repository of Python packages


# python -m pip install PACKAGE
# ↓
# Install package


# pip list
# ↓
# Show installed packages


# pip show PACKAGE
# ↓
# Show package details


# pip uninstall PACKAGE
# ↓
# Remove package


# pip freeze
# ↓
# Show packages in requirements format


# pip freeze > requirements.txt
# ↓
# Save dependencies


# pip install -r requirements.txt
# ↓
# Install dependencies from file


# python -m venv .venv
# ↓
# Create virtual environment


# activate
# ↓
# Start using virtual environment


# deactivate
# ↓
# Leave virtual environment


# .gitignore
# ↓
# Prevent files/folders from being tracked by Git


# .env
# ↓
# Common place for project configuration/secrets


# =====================================================
# MOST IMPORTANT COMMANDS
# =====================================================


# CHECK PIP:
#
# python -m pip --version


# INSTALL:
#
# python -m pip install requests


# LIST:
#
# python -m pip list


# SHOW:
#
# python -m pip show requests


# UNINSTALL:
#
# python -m pip uninstall requests


# CREATE VENV:
#
# python -m venv .venv


# WINDOWS POWERSHELL ACTIVATE:
#
# .\.venv\Scripts\Activate.ps1


# WINDOWS CMD ACTIVATE:
#
# .venv\Scripts\activate.bat


# MAC / LINUX ACTIVATE:
#
# source .venv/bin/activate


# DEACTIVATE:
#
# deactivate


# SAVE DEPENDENCIES:
#
# python -m pip freeze > requirements.txt


# INSTALL DEPENDENCIES:
#
# python -m pip install -r requirements.txt


# =====================================================
# INTERVIEW QUESTIONS & ANSWERS
# =====================================================

print("\n" + "=" * 60)
print("INTERVIEW QUESTIONS & ANSWERS")
print("=" * 60)


# =====================================================
# Q1. What is pip?
# =====================================================

# Answer:
#
# pip is Python's package installer.
#
# It is used to install, upgrade and uninstall
# external Python packages.


# =====================================================
# Q2. What is PyPI?
# =====================================================

# Answer:
#
# PyPI means Python Package Index.
#
# It is a repository where Python packages
# are published and from which pip commonly
# downloads packages.


# =====================================================
# Q3. What is the difference between a built-in
# module and an external package?
# =====================================================

# Answer:
#
# Built-in / standard-library module:
# → Comes with Python installation.
#
# Example:
# math
# datetime
# random
#
#
# External package:
# → Installed separately.
#
# Example:
# requests
# pandas
# fastapi


# =====================================================
# Q4. What is a virtual environment?
# =====================================================

# Answer:
#
# A virtual environment is an isolated Python
# environment for a project.
#
# It allows each project to have its own
# packages and package versions.


# =====================================================
# Q5. Why should we use a virtual environment?
# =====================================================

# Answer:
#
# To:
#
# isolate dependencies
# avoid version conflicts
# keep projects clean
# make environments reproducible


# =====================================================
# Q6. How do you create a virtual environment?
# =====================================================

# Answer:
#
# python -m venv .venv


# =====================================================
# Q7. How do you activate a virtual environment?
# =====================================================

# Answer:
#
# Windows PowerShell:
#
# .\.venv\Scripts\Activate.ps1
#
#
# macOS/Linux:
#
# source .venv/bin/activate


# =====================================================
# Q8. How do you deactivate a virtual environment?
# =====================================================

# Answer:
#
# deactivate


# =====================================================
# Q9. What is requirements.txt?
# =====================================================

# Answer:
#
# requirements.txt contains project dependencies,
# usually including package versions.
#
# It helps reproduce a project's Python environment.


# =====================================================
# Q10. How do you generate requirements.txt?
# =====================================================

# Answer:
#
# python -m pip freeze > requirements.txt


# =====================================================
# Q11. How do you install packages from
# requirements.txt?
# =====================================================

# Answer:
#
# python -m pip install -r requirements.txt


# =====================================================
# Q12. Difference between pip list and pip freeze?
# =====================================================

# Answer:
#
# pip list
# → Shows installed packages in a readable table.
#
#
# pip freeze
# → Produces requirements-style package output
#   such as:
#
# package==version


# =====================================================
# Q13. Why use python -m pip instead of pip?
# =====================================================

# Answer:
#
# python -m pip helps ensure we use pip associated
# with the selected Python interpreter.
#
# This can avoid confusion when multiple Python
# installations/environments exist.


# =====================================================
# Q14. Should .venv be committed to GitHub?
# =====================================================

# Answer:
#
# Normally no.
#
# Add:
#
# .venv/
#
# to .gitignore.
#
# Commit dependency files such as
# requirements.txt instead.


# =====================================================
# Q15. What is .env?
# =====================================================

# Answer:
#
# .env is commonly used for configuration values
# such as database URLs, API keys and secret keys.
#
# Real secrets should normally not be committed
# to source control.


# =====================================================
# Q16. Difference between .venv and .env?
# =====================================================

# Answer:
#
# .venv
# ↓
# Virtual Python environment
# containing Python + installed packages.
#
#
# .env
# ↓
# Configuration values / environment variables.
#
#
# They are COMPLETELY different things.


# =====================================================
# VERY COMMON INTERVIEW TRAP
# =====================================================

# .venv ≠ .env


# .venv
# → Python environment


# .env
# → Configuration / secrets


# =====================================================
# Q17. What happens if two projects need different
# versions of the same package?
# =====================================================

# Answer:
#
# Use separate virtual environments.
#
# Example:
#
# Project A
# → package version 1
#
# Project B
# → package version 2
#
# Each project's environment remains isolated.


# =====================================================
# Q18. How can you check which Python interpreter
# your program is using?
# =====================================================

# Answer:

# import sys
#
# print(sys.executable)


# =====================================================
# Q19. How can we check whether Python is currently
# running inside a virtual environment?
# =====================================================

# Answer:

# import sys
#
# is_venv = sys.prefix != sys.base_prefix
#
# print(is_venv)


# =====================================================
# Q20. What is a dependency?
# =====================================================

# Answer:
#
# A dependency is a package/library required
# by a project or another package to function.


# =====================================================
# REAL INTERVIEW ANSWER
# =====================================================

# Interviewer:
#
# "How do you normally start a new Python project?"


# Good Answer:
#
# 1. Create a project directory.
#
# 2. Create a virtual environment using:
#
#    python -m venv .venv
#
# 3. Activate the environment.
#
# 4. Install required packages with pip.
#
# 5. Keep dependencies in requirements.txt
#    or the project's dependency-management file.
#
# 6. Add .venv and secret files to .gitignore.
#
# 7. Select the virtual environment interpreter
#    in the IDE.


# =====================================================
# INTERVIEW QUICK REVISION
# =====================================================

# MUST KNOW:


# 1.
# What is pip?


# 2.
# What is PyPI?


# 3.
# What is a virtual environment?


# 4.
# Why use virtual environments?


# 5.
# How to create / activate / deactivate venv?


# 6.
# What is requirements.txt?


# 7.
# pip list vs pip freeze?


# 8.
# How to install requirements.txt?


# 9.
# .venv vs .env?


# 10.
# Why should .venv not normally be uploaded
# to GitHub?


# =====================================================
# FINAL SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print(
    "pip → Install and manage Python packages"
)

print(
    "PyPI → Python package repository"
)

print(
    "venv → Isolated Python project environment"
)

print(
    "requirements.txt → Project dependencies"
)

print(
    ".env → Project configuration / secrets"
)

print(
    ".gitignore → Ignore files from Git tracking"
)


print("\nTopic 23 Complete")