import os
from datetime import datetime

FILE_NAME = "expenses.txt"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip().split(",") for line in file.readlines()]

def save_expense(date, category, amount, description):
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    save_expense(date, category, amount, description)
    print("Expense added.\n")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.\n")
        return
    print("\nAll Expenses:")
    for exp in expenses:
        print(f"Date: {exp[0]} | Category: {exp[1]} | Amount: {exp[2]} | Note: {exp[3]}")
    print()

def view_total():
    expenses = load_expenses()
    total = sum(float(exp[2]) for exp in expenses)
    print(f"\nTotal Expenses: {total}\n")

def monthly_summary():
    expenses = load_expenses()
    month = input("Enter month (YYYY-MM): ")

    filtered = [exp for exp in expenses if exp[0].startswith(month)]
    total = sum(float(exp[2]) for exp in filtered)

    print(f"\nTotal for {month}: {total}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()