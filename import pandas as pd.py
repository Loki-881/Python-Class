import pandas as pd
from datetime import datetime

# Expense class
class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "Name": self.name,
            "Amount": self.amount,
            "Category": self.category,
            "Date": self.date
        }

# Functions
def add_expense():
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        category = input("Enter category (Food, Travel, Shopping, etc.): ")
        date = datetime.now().strftime("%Y-%m-%d")

        expense = Expense(name, amount, category, date)

        df = pd.DataFrame([expense.to_dict()])
        df.to_csv("expenses.csv", mode="a", header=not pd.io.common.file_exists("expenses.csv"), index=False)
        print("✅ Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def view_expenses():
    try:
        df = pd.read_csv("expenses.csv")
        print("\n📒 All Expenses:\n", df)
    except FileNotFoundError:
        print("No expenses recorded yet.")

def monthly_summary():
    try:
        df = pd.read_csv("expenses.csv")
        df["Date"] = pd.to_datetime(df["Date"])
        df["Month"] = df["Date"].dt.to_period("M")

        print("\n📊 Monthly Total Expenses:")
        print(df.groupby("Month")["Amount"].sum())

        print("\n📊 Category-wise Summary:")
        print(df.groupby("Category")["Amount"].sum())
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main menu
def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Exiting... Goodbye 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
