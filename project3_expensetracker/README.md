# 💰 Expense Tracker (Python)

A simple **command-line Expense Tracker** built in Python.  
This program allows you to **add expenses, list them, calculate totals, and filter by category**.  
It demonstrates the use of **functions, lists, dictionaries, loops, conditionals, and lambda functions** in Python.

---

## 🚀 Features

- ✅ Add an expense (with amount + category)
- ✅ View all expenses
- ✅ Calculate total expenses
- ✅ Filter expenses by category
- ✅ Exit program safely

---

## 🛠️ How to Run

1. Save the code in a file called `expense_tracker.py`
2. Run the program with:

```bash
python expense_tracker.py
```

3. Follow the on-screen menu to interact with the program.

---

## 📂 Code Structure

- `add_expense(expenses, amount, category)` → Adds an expense to the list.  
- `print_expenses(expenses)` → Displays all expenses in a readable format.  
- `total_expenses(expenses)` → Calculates the sum of all expense amounts.  
- `filter_expenses_by_category(expenses, category)` → Returns only expenses in a given category.  
- `main()` → Handles program flow, user input, and menu system.  

---

## ✨ Example Usage

```
Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 1
Enter amount: 75
Enter category: Transport

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 2

All Expenses:
Amount: 75.0, Category: Transport

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 3

Total Expenses:  75.0
```

---

## 🧠 Concepts Used

- **Lists & Dictionaries** → store expenses as `{'amount': X, 'category': Y}`
- **Functions** → modular code design
- **Lambda Functions** → extract and filter data efficiently
- **map() & filter()** → apply functional programming techniques
- **while loop** → menu runs until user exits
- **Conditionals** → process user choices

---

👨‍💻 Author: *Your Name Here*
olaleye faheem 