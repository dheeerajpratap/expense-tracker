import json

expenses = []

def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})
    print(f"Added: {name} - ₹{amount}")

def view_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ₹{total}")

def save_to_file():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)
    print("Expenses saved!")

def load_from_file():
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
        print("Expenses loaded!", expenses)
    except FileNotFoundError:
        print("No saved expenses found.")

add_expense("Food", 150)
add_expense("Travel", 50)
view_total()
save_to_file()
load_from_file() 
