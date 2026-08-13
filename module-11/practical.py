import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# --- DSA Core Functions (Procedural Linked Array Simulation) ---

def create_expense_record(expense_id, amount, category, date, description):
    """Returns a dynamic dictionary representing an expense structure."""
    return {
        "id": int(expense_id),
        "amount": float(amount),
        "category": str(category),
        "date": str(date),
        "description": str(description)
    }

def delete_expense_record(expense_list, expense_id):
    """Algorithm: Linear Search & Eviction to delete a record by ID."""
    target_index = -1
    
    # Sequential lookup loop
    for i in range(len(expense_list)):
        if expense_list[i]["id"] == expense_id:
            target_index = i
            break
            
    if target_index != -1:
        expense_list.pop(target_index)
        return True # Delete successful
    return False # ID not found

def get_next_id(expense_list):
    """Algorithm: Dynamic Max Accumulator to find the next unique ID."""
    if not expense_list:
        return 1
    max_id = 0
    for expense in expense_list:
        if expense["id"] > max_id:
            max_id = expense["id"]
    return max_id + 1

# --- File Handling & Storage Processing ---

def initialize_file():
    """Creates the CSV schema if the file does not exist on disk."""
    if not os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
        except IOError as e:
            print(f"❌ Storage Initialization Error: {e}")

def load_data():
    """Parses CSV rows into the local tracking list structure."""
    expense_list = []
    if not os.path.exists(FILE_NAME):
        return expense_list

    try:
        with open(FILE_NAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = create_expense_record(
                    row["ID"], 
                    row["Amount"], 
                    row["Category"], 
                    row["Date"], 
                    row["Description"]
                )
                expense_list.append(record)
    except (IOError, ValueError, KeyError) as e:
        print(f"❌ File Parsing Error: Malformed data or file locked. {e}")
    return expense_list

def save_data(expense_list):
    """Serializes and overwrites data back to the persistent CSV layer."""
    try:
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
            
            for exp in expense_list:
                writer.writerow([exp["id"], exp["amount"], exp["category"], exp["date"], exp["description"]])
    except IOError as e:
        print(f"❌ Data Saving Error: Could not write to disk. {e}")

# --- User Interaction / UI Functions ---

def add_expense_ui(expense_list):
    """Captures, validates, and appends user inputs."""
    print("\n--- Add New Expense ---")
    
    # 1. Amount Validation Loop
    while True:
        try:
            amount = float(input("Enter amount spent: "))
            if amount <= 0:
                print("⚠️ Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid entry. Please input a numerical currency amount.")

    category = input("Enter category (e.g., Food, Travel, Rent): ").strip().title()
    if not category:
        category = "Miscellaneous"

    # 2. Date Validation Loop
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_input:
            date = datetime.today().strftime('%Y-%m-%d')
            break
        try:
            datetime.strptime(date_input, '%Y-%m-%d')
            date = date_input
            break
        except ValueError:
            print("⚠️ Incorrect date configuration. Use strict YYYY-MM-DD format.")

    description = input("Enter description details: ").strip()
    if not description:
        description = "N/A"

    # Process and push data
    new_id = get_next_id(expense_list)
    new_record = create_expense_record(new_id, amount, category, date, description)
    expense_list.append(new_record)
    save_data(expense_list)
    print(f"✅ Record created! (Assigned ID: {new_id})")

def view_expenses_ui(expense_list):
    """Outputs table layout of ledger records."""
    print("\n--- Current Expense Logs ---")
    if not expense_list:
        print("📭 Ledger empty. No transactions recorded.")
        return

    print(f"{'ID':<5} | {'Amount':<10} | {'Category':<15} | {'Date':<12} | {'Description'}")
    print("-" * 65)
    
    total_spend = 0.0
    for exp in expense_list:
        print(f"{exp['id']:<5} | ${exp['amount']:<9.2f} | {exp['category']:<15} | {exp['date']:<12} | {exp['description']}")
        total_spend += exp['amount']
        
    print("-" * 65)
    print(f"Aggregated System Total: ${total_spend:.2f}")

def delete_expense_ui(expense_list):
    """Handles operational routing for record removal."""
    print("\n--- Delete Expense Record ---")
    try:
        target_id = int(input("Enter target item ID to delete: "))
        if delete_expense_record(expense_list, target_id):
            save_data(expense_list)
            print(f"🗑️ Record ID {target_id} successfully purged from storage.")
        else:
            print(f"⚠️ Process Failed: ID {target_id} does not exist.")
    except ValueError:
        print("⚠️ Format Error: Transaction ID entry must be an integer.")

def generate_report_ui(expense_list):
    """Algorithm: Hash-Map accumulation parsing unique keys."""
    print("\n--- Categorical Allocation Report ---")
    if not expense_list:
        print("📭 Analytical report unavailable: missing core data.")
        return

    category_map = {}
    for exp in expense_list:
        cat = exp["category"]
        category_map[cat] = category_map.get(cat, 0.0) + exp["amount"]

    print(f"{'Category Group':<18} | {'Total Volume'}")
    print("-" * 35)
    for cat, allocation in category_map.items():
        print(f"{cat:<18} | ${allocation:.2f}")

# --- Core Runtime Logic Loop ---

def main():
    initialize_file()
    # In-memory storage state array
    global_expense_memory = load_data()

    while True:
        print("\n=== EXPENSE TRACKER (PROCEDURAL ENGINE) ===")
        print("1. Log New Expense")
        print("2. Display All Records")
        print("3. Delete Record by ID")
        print("4. Calculate Category Summary")
        print("5. Terminate Application")
        
        user_choice = input("Execute selection (1-5): ").strip()
        
        if user_choice == '1':
            add_expense_ui(global_expense_memory)
        elif user_choice == '2':
            view_expenses_ui(global_expense_memory)
        elif user_choice == '3':
            delete_expense_ui(global_expense_memory)
        elif user_choice == '4':
            generate_report_ui(global_expense_memory)
        elif user_choice == '5':
            print("💾 Memory cleared. Persistent states saved. Goodbye!")
            break
        else:
            print("⚠️ System Warning: Invalid execution digit. Enter 1-5 only.")

if __name__ == "__main__":
    main()




