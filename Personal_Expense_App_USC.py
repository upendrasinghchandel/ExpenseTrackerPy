# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:49:48 2024

@author: Upendra Singh Chandel
"""

import json
from datetime import datetime

# Load data from a file if it exists, otherwise create a new expense data structure
def load_data(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"expenses": [], "budgets": {}}

# Save data to a file
def save_data(data, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Add a new expense
def add_expense(data):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent, Utilities): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    data["expenses"].append(expense)
    print("Expense added successfully.")

# Display all expenses
def display_expenses(data):
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        print("\n--- All Expenses ---")
        for expense in data["expenses"]:
            print(f"Date: {expense['date']}, Category: {expense['category']}, "
                  f"Amount: {expense['amount']}, Description: {expense['description']}")

# Set a monthly budget for a specific category
def set_budget(data):
    category = input("Enter category to set budget for: ")
    amount = float(input("Enter budget amount: "))
    data["budgets"][category] = amount
    print(f"Budget set for {category}: {amount}")

# View the current budget and spending
def view_budget(data):
    if not data["budgets"]:
        print("No budgets set yet.")
    else:
        print("\n--- Budgets ---")
        for category, budget in data["budgets"].items():
            total_spent = sum(expense["amount"] for expense in data["expenses"] if expense["category"] == category)
            print(f"Category: {category}, Budget: {budget}, Spent: {total_spent}, Remaining: {budget - total_spent}")

# Interactive menu
def main():
    data = load_data()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Set Monthly Budget")
        print("4. View Budgets and Spending")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(data)
        elif choice == "2":
            display_expenses(data)
        elif choice == "3":
            set_budget(data)
        elif choice == "4":
            view_budget(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
