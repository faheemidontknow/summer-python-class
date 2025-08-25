# Function to add a new expense
# expenses → list where all expenses are stored
# amount → money spent
# category → type of expense (like Food, Transport, etc.)
def add_expense(expenses, amount, category):
    # Add a dictionary with amount and category to the expenses list
    expenses.append({'amount': amount, 'category': category})
    

# Function to print all expenses in a nice format
def print_expenses(expenses):
    # Loop through each expense dictionary in the list
    for expense in expenses:
        # Print the amount and category of the expense
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    

# Function to calculate total expenses
def total_expenses(expenses):
    # Use map() with a lambda function to extract amounts
    # sum() then adds all those amounts together
    return sum(map(lambda expense: expense['amount'], expenses))
    

# Function to filter expenses by a given category
def filter_expenses_by_category(expenses, category):
    # Return only expenses that match the given category
    return filter(lambda expense: expense['category'] == category, expenses)
    

# Main function that runs the Expense Tracker program
def main():
    # Start with an empty expenses list
    expenses = []

    # Infinite loop → program keeps running until user exits
    while True:
        # Print the menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Ask the user for their choice
        choice = input('Enter your choice: ')

        # ---- OPTION 1: Add Expense ----
        if choice == '1':
            # Ask user for amount (convert input to float for decimals)
            amount = float(input('Enter amount: '))
            # Ask user for category
            category = input('Enter category: ')
            # Add the new expense to the list
            add_expense(expenses, amount, category)

        # ---- OPTION 2: View All Expenses ----
        elif choice == '2':
            print('\nAll Expenses:')
            # Show all the expenses recorded
            print_expenses(expenses)
    
        # ---- OPTION 3: Total Expenses ----
        elif choice == '3':
            # Show the total amount of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        # ---- OPTION 4: Filter by Category ----
        elif choice == '4':
            # Ask which category the user wants to see
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # Filter expenses by category
            expenses_from_category = filter_expenses_by_category(expenses, category)
            # Print only the filtered expenses
            print_expenses(expenses_from_category)
    
        # ---- OPTION 5: Exit ----
        elif choice == '5':
            print('Exiting the program.')
            break  # End the loop → program stops
