import csv
import os

FILENAME = 'expenses.csv'

def add_expense():
    description = input("Enter description: ")
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., Food, Transport, Other): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount, category])
    print("Expense added!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_by_category():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    totals = {}
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 3:
                continue
            category = row[2]
            amount = float(row[1])
            totals[category] = totals.get(category, 0) + amount

    print("\nTotal by category:")
    for cat, total in totals.items():
        print(f"{cat}: £{total:.2f}")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total by Category")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
