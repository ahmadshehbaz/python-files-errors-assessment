# 🏫 Institute Management Tools

<div align="center">

# 📊 Institute Management System

### Expense Tracking & Student Attendance Cleaning

A beginner-friendly Python project demonstrating file handling, exception handling, sets, and list comprehensions through two practical institute management applications.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Project](https://img.shields.io/badge/Project-Beginner%20Friendly-orange)

<br/>

<a href="https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/">
  <img src="https://img.shields.io/badge/🌐_View_Live_Demo-Click_Here-blue?style=for-the-badge" alt="Live Demo"/>
</a>

**Built with Python 🐍**

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Applications](#-applications)
- [Technologies Used](#-technologies-used)
- [How to Run](#-how-to-run)
- [Error Handling](#-error-handling)
- [Sets and List Comprehensions](#-sets-and-list-comprehensions)
- [Sample Execution](#-sample-execution)
- [Test Cases](#-test-cases)
- [Expected Output Files](#-expected-output-files)
- [Learning Outcomes](#-learning-outcomes)

---

## 🎯 Overview

The Institute Management Tools project contains two independent Python applications designed to simplify daily administrative tasks in a training institute.

The project focuses on practical Python programming concepts, including:

- File handling (reading and writing files).
- Exception handling.
- Lists and dictionaries.
- Sets.
- List comprehensions.
- Loops and conditional statements.
- Functions.
- CSV file management.

### Main Objectives

1. Record and manage daily institute expenses.
2. Calculate total expenses by category.
3. Clean student attendance records.
4. Remove duplicate student names.
5. Generate organized and sorted attendance records.
6. Store information permanently using files.

---

## 📁 Project Structure

```text
python-files-errors-assessment/
│
├── expense_tracker.py
│
├── attendance_cleaner.py
│
├── attendance.txt
│
├── expenses.csv
│
├── attendance_clean.csv
│
└── README.md
```

**File descriptions:**

| File | Purpose |
|---|---|
| `expense_tracker.py` | Manages institute expenses |
| `attendance_cleaner.py` | Cleans student attendance |
| `attendance.txt` | Original student records |
| `expenses.csv` | Stores expense records |
| `attendance_clean.csv` | Stores cleaned attendance |
| `README.md` | Project documentation |

Note: `expenses.csv` and `attendance_clean.csv` are generated automatically when their respective programs run.

---

## 🧩 Applications

### 1. 💰 Institute Expense Tracker

**File:** `expense_tracker.py`

The Expense Tracker helps institute administration record and manage daily operational expenses.

It stores expense information in a CSV file so records remain available even after closing the program.

**Features:**

- Add new expenses.
- View all saved expenses.
- Calculate total expenses by category.
- Display unique expense categories.
- Validate numerical expense amounts.
- Save expense records in `expenses.csv`.
- Load previously saved records when the program starts.

**Expense information includes:**

| Field | Description |
|---|---|
| Date | Expense date |
| Item | Purchased item or service |
| Category | Expense category |
| Amount | Expense amount |

**Available Menu:**

```text
===== Institute Expense Tracker =====

1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit
```

### 2. 🎓 Student Attendance Cleaner

**File:** `attendance_cleaner.py`

The Attendance Cleaner organizes student names stored in a text file.

It removes unnecessary spaces, fixes inconsistent capitalization, removes duplicate names, and sorts the final attendance list alphabetically.

**Features:**

- Read names from `attendance.txt`.
- Remove unnecessary spaces using `strip()`.
- Standardize capitalization using `title()`.
- Remove duplicate names using sets.
- Count unique students.
- Sort names alphabetically.
- Save cleaned records in `attendance_clean.csv`.

**Example:**

Original records:

```text
ali
AHMAD
sara
Ali
  zain
SARA
hamza
ahmad
```

Cleaned records:

```text
Ahmad
Ali
Hamza
Sara
Zain
```

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CSV Module | Reading and writing CSV files |
| File Handling | Storing and retrieving records |
| Exception Handling | Managing runtime errors |
| Lists | Storing multiple records |
| Dictionaries | Organizing expense information |
| Sets | Removing duplicate values |
| List Comprehensions | Cleaning student names |

No external Python packages are required.

---

## 🚀 How to Run

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Check your installation:

```bash
python --version
```

### Step 2: Open Project Folder

Open your terminal inside the project directory.

### Step 3: Run Expense Tracker

```bash
python expense_tracker.py
```

Select an option from the menu.

### Step 4: Run Attendance Cleaner

Make sure `attendance.txt` exists in the project folder.

Run:

```bash
python attendance_cleaner.py
```

The program will generate:

```text
attendance_clean.csv
```

---

## ⚠️ Error Handling

Exception handling prevents programs from crashing when something unexpected happens.

This project handles the following errors:

### 1. FileNotFoundError

**Where:** Both Python applications.

**Problem:**

The program tries to open a file that does not exist.

**Expense Tracker:**

```python
try:
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

except FileNotFoundError:
    print("No previous expense file found.")
```

**Why is it handled?**

When the program runs for the first time, `expenses.csv` may not exist.

Instead of crashing, the program starts with an empty expense list.

The Attendance Cleaner also catches this error if `attendance.txt` is missing and displays a helpful message.

### 2. ValueError

**Where:** Expense Tracker.

**Problem:**

The user enters text instead of a valid numerical amount.

Example:

```text
Enter amount: abc
```

**Code:**

```python
try:
    amount = float(input("Enter amount: "))

except ValueError:
    print("Please enter a valid number.")
```

**Why is it handled?**

Python cannot convert invalid text such as `abc` into a floating-point number.

The program catches the error and asks the user to enter the amount again.

---

## 🧠 Sets and List Comprehensions

These are important Python concepts used in this project.

### 1. Sets

A set stores unique values. It automatically removes duplicates.

**Example from Expense Tracker:**

```python
categories = {
    expense["category"]
    for expense in expenses
}
```

**Explanation:**

- `expenses` contains all expense records.
- The loop visits each expense.
- `expense["category"]` gets its category.
- The set stores each category only once.

Example:

```python
categories = {"Stationery", "Internet", "Stationery"}
```

Result:

```python
{"Stationery", "Internet"}
```

**Example from Attendance Cleaner:**

```python
unique_names = set(cleaned_names)
```

This converts the cleaned student list into a set and removes duplicate names.

### 2. List Comprehension

List comprehension creates a new list in a short and readable way.

**Example from Attendance Cleaner:**

```python
cleaned_names = [
    name.strip().title()
    for name in original_names
    if name.strip()
]
```

**Explanation:**

- `for name in original_names` visits every student name.
- `name.strip()` removes unnecessary spaces.
- `name.title()` converts names into title case.
- `if name.strip()` ignores empty lines.

Example:

Input:

```python
[" ali ", "AHMAD", " sara "]
```

Output:

```python
["Ali", "Ahmad", "Sara"]
```

---

## 💻 Sample Execution

### Expense Tracker: Saving Data

First, run:

```bash
python expense_tracker.py
```

Example interaction:

```text
===== Institute Expense Tracker =====

1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit

Choose an option (1-4): 1

--- Add New Expense ---

Enter date: 2026-11-15
Enter item name: Notebooks
Enter category: Stationery
Enter amount: 500

Expense saved successfully.
```

Add another expense:

```text
Choose an option (1-4): 1

Enter date: 2026-11-15
Enter item name: Internet Bill
Enter category: Internet
Enter amount: 2000

Expense saved successfully.
```

### Checking Saved CSV Data

The program automatically creates `expenses.csv`.

Its contents will look like:

```csv
date,item,category,amount
2026-11-15,Notebooks,Stationery,500.0
2026-11-15,Internet Bill,Internet,2000.0
```

### Loading Previously Saved Data

Now close the program and run it again:

```bash
python expense_tracker.py
```

Select:

```text
Choose an option (1-4): 2
```

Expected output:

```text
--- All Expenses ---

Categories: Internet, Stationery

1. Date: 2026-11-15 | Item: Notebooks | Category: Stationery | Amount: 500.00

2. Date: 2026-11-15 | Item: Internet Bill | Category: Internet | Amount: 2000.00
```

**Result:** Previously saved expenses are successfully loaded from the CSV file.

### Calculating Category Totals

Select option 3:

```text
Choose an option (1-4): 3
```

Expected output:

```text
--- Total Expenses by Category ---

Internet: 2000.00
Stationery: 500.00
```

---

## 🧪 Test Cases

The following test cases can be used to verify both applications.

### Expense Tracker Test Cases

| Test | Input / Condition | Expected Result |
|---|---|---|
| 1 | Add a valid expense | Expense saved |
| 2 | Enter `abc` as amount | ValueError handled |
| 3 | Enter `250.50` | Decimal amount accepted |
| 4 | Start without expenses.csv | Empty list created |
| 5 | Restart program | Previous expenses loaded |
| 6 | Add multiple categories | Unique categories displayed |
| 7 | Calculate category totals | Correct totals displayed |
| 8 | Enter negative amount | User asked to try again |

### Attendance Cleaner Test Cases

| Test | Input / Condition | Expected Result |
|---|---|---|
| 1 | Duplicate student names | Duplicates removed |
| 2 | Uppercase names | Converted to title case |
| 3 | Extra spaces | Spaces removed |
| 4 | Empty lines | Ignored |
| 5 | Unsorted names | Alphabetically sorted |
| 6 | Missing attendance.txt | FileNotFoundError handled |
| 7 | Empty attendance file | Empty cleaned list generated |
| 8 | Repeated names with different capitalization | Only one unique name remains |

---

## 📂 Expected Output Files

After running both applications, the project will contain:

**expenses.csv**

Stores all expense records.

**attendance_clean.csv**

Stores unique and alphabetically sorted student names.

Both files are generated automatically by their respective Python programs.

---

## 🎓 Learning Outcomes

By completing this project, you will understand:

- How to read and write files in Python.
- How to work with CSV files.
- How to handle `FileNotFoundError` and `ValueError`.
- How to use sets to remove duplicate records.
- How to use list comprehensions.
- How to organize data using lists and dictionaries.
- How to build practical command-line applications.

---

## 👨‍💻 Author

**Python Beginner Project**

Developed as part of a Python programming assessment.

---

<div align="center">

### ⭐ Thank You for Visiting!

**Keep Learning. Keep Coding. Keep Building. 🐍**

</div>
