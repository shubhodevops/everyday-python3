''' Author: Saif A Khan Shubho, Date: 12 August 2026 '''
import random, csv , string , os
from datetime import datetime
app_name = "Welcome to Smart File-Based Manager"

def generate_id(length=8):
    alphanum = string.ascii_uppercase + string.digits
    return "".join(random.choices(alphanum, k=length))


def print_app_name():
    print("─" * 40)
    print(f"   {app_name}")
    print("─" * 40)


def error_input():
    # \033[91m sets red text, \033[0m resets color
    print("\033[91m✘ Error: Invalid input. Please try again.\033[0m")


def clear_screen():

    print("\n" * 100)


def display_menu():
    print("\nMain Menu::\n")
    menu_items = ["Add new expense", "View all expenses", "Add new note", "View all notes", "Exit"]
    for index, item in enumerate(menu_items, start=1):
        print(f"    {index}› {item}")
        print("─" * 30)


def add_expense():
    exp_title = input("Enter expense title: ").strip().title()
    while True:
        try:
            amount = float(input("Enter amount (BDT): "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            error_input()

    exp_id = generate_id()
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_exists = os.path.exists("expenses.csv")

    with open("expenses.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ExpID", "ExpTitle", "Amount", "TransDate"])
        writer.writerow([exp_id, exp_title, f"{amount:.2f}", current_date])
    print("\n[SUCCESS] Expense recorded successfully!")


def view_all_expenses():
    clear_screen()
    try:
        with open("expenses.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            print("═" * 60)
            print(f"{'ID':<10}  {'Expense Title':<20}  {'Amount':<10}  {'Date':<12}")
            print("─" * 60)
            total_amount = 0.0
            record_count = 0
            for row in reader:
                if len(row) == 4:
                    exp_id, title, amount, date = row
                    print(f"{exp_id:<10}  {title:<20}  {float(amount):<10.2f}  {date:<15}")
                    total_amount += float(amount)
                    record_count += 1
            print("═" * 60)
            print(f"Total Records: {record_count} | Overall Total: {total_amount:.2f} BDT")
            print("═" * 60)

            input("\nPress Enter to return to the Main Menu...")
            clear_screen()
    except FileNotFoundError:
        print("\n\033[93m⚠ Info: No expenses recorded yet. The file 'expenses.csv' does not exist.\033[0m")


def add_note():
    note_content = input("Enter your note: ").strip()
    if not note_content:
        print("Note cannot be empty!")
        return

    note_id = generate_id()
    current_time = datetime.now().strftime("%Y-%m-%d")



    with open("notes.txt", mode="a", encoding="utf-8") as file:
        file.write(f"[{note_id}] {current_time} - {note_content}\n")
    print("\n[SUCCESS] Note saved successfully!")


def view_all_notes():
    clear_screen()
    try:
        with open("notes.txt", mode="r", encoding="utf-8") as file:
            print("Saved Notes:")
            print("─" * 50)
            notes = file.readlines()
            for note in notes:
                print(note.strip())
            print("─" * 50)

            input("\nPress Enter to return to the Main Menu...")
            clear_screen()
    except FileNotFoundError:
        print("\n\033[93m⚠ Info: No notes saved yet. The file 'notes.txt' does not exist.\033[0m")


def smart_manager():
    while True:
        display_menu()
        try:
            selection = int(input("Enter selection between 1 to 5: "))
        except ValueError:
            error_input()
            continue

        if selection == 5:
            print("─" * 45)
            print("Thank you for using Smart File-Based Manager. Goodbye!")
            print("─" * 45)
            break
        elif selection == 1:
            clear_screen()
            print("─" * 30)
            print("Add New Expense Entry:\n")
            add_expense()
            print("─" * 30)
        elif selection == 2:
            view_all_expenses()
        elif selection == 3:
            clear_screen()
            print("─" * 30)
            print("Add New Note:\n")
            add_note()
            print("─" * 30)
        elif selection == 4:
            view_all_notes()
        else:
            error_input()


def main():
    clear_screen()
    print_app_name()
    smart_manager()


if __name__ == "__main__":
    main()
