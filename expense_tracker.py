import csv
from pathlib import Path

FILE_NAME = "expenses.csv"
FIELD_NAMES = ["date", "item", "category", "amount"]


def load_expenses():
    """Load saved expenses. Return an empty list if the file does not exist."""
    expenses = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Convert the saved amount from text to a number.
                row["amount"] = float(row["amount"])
                expenses.append(row)

    except FileNotFoundError:
        print("No previous expense file found. Starting with an empty list.")

    return expenses


def save_expenses(expenses):
    """Save all expenses to the CSV file."""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(expenses)


def get_amount():
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number, such as 250 or 250.50.")


def add_expense(expenses):
    print("\n--- Add New Expense ---")
    date = input("Enter date (e.g. 2026-11-15): ").strip()
    item = input("Enter item name: ").strip()
    category = input("Enter category: ").strip().title()
    amount = get_amount()

    expense = {
        "date": date,
        "item": item,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense saved successfully.")


def show_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses have been recorded yet.")
        return

    # A set keeps only unique category names.
    categories = {expense["category"] for expense in expenses}
    print("Categories:", ", ".join(sorted(categories)))

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. Date: {expense['date']} | "
            f"Item: {expense['item']} | "
            f"Category: {expense['category']} | "
            f"Amount: {expense['amount']:.2f}"
        )


def show_category_totals(expenses):
    print("\n--- Total Expenses by Category ---")

    if not expenses:
        print("No expenses available to calculate.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    for category, total in sorted(totals.items()):
        print(f"{category}: {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Institute Expense Tracker =====")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_category_totals(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
