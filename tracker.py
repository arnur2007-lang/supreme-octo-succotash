import csv
from datetime import datetime

FILENAME = 'data.csv'

# Create the CSV file with header if it doesn't exist
try:
    with open(FILENAME, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Type', 'Category', 'Amount'])
except FileExistsError:
    pass

# Add a new record to the file
def add_record():
    entry_type = input("Input type (Income/Expense): ").strip().capitalize()
    category = input("Enter category (e.g., food, transport): ").strip()
    amount = input("Enter amount: ").strip()
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, entry_type, category, amount])

    print("\nRecord added successfully.\n")

# Read and display all records
def read_record():
    with open(FILENAME, 'r') as file:
        print("\nAll Records:\n")
        print(file.read())

# Show summary: total income, expenses, and savings
def summary_report():
    income = 0.0
    expenses = 0.0

    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                amount = float(row['Amount'])
                if row['Type'].lower() == 'income':
                    income += amount
                elif row['Type'].lower() == 'expense':
                    expenses += amount
            except ValueError:
                continue  # Skip rows with invalid numeric input

    savings = income - expenses

    print("\nSummary Report:")
    print("Total Income   :", "$" + str(round(income, 2)))
    print("Total Expenses :", "$" + str(round(expenses, 2)))
    print("Savings        :", "$" + str(round(savings, 2)), "\n")

# Menu
print("Welcome to Budget Tracker")
choice = input("What action do you want to perform?\n1. Add record\n2. View all records\n3. Summary report\n> ")

if choice == '1':
    add_record()
elif choice == '2':
    read_record()
elif choice == '3':
    summary_report()
else:
    print("Invalid choice. Please select 1, 2, or 3.")


