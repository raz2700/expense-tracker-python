# tracker.py
import json
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    description = input("Enter a description: ")
    amount = float(input("Enter the amount: £"))
    category = input("Enter a category: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.\n")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.\n")
        return

    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} - £{e['amount']:.2f} - {e['category']} - {e['description']}")
    print()

def main():
    while True:
        print("== Expense Tracker ==")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
