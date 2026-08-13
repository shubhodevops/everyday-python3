"""Smart File-Based Manager."""

from __future__ import annotations

import csv
import logging
import os
import secrets
import string
from dataclasses import asdict, dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Callable

APP_NAME = "Smart File-Based Manager"
DATA_DIR = Path("data")
EXPENSES_FILE = DATA_DIR / "expenses.csv"
NOTES_FILE = DATA_DIR / "notes.txt"

EXPENSE_FIELDS = ["ExpID", "ExpTitle", "Amount", "TransDate"]

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Expense:
    exp_id: str
    title: str
    amount: Decimal
    trans_date: date


@dataclass(frozen=True)
class Note:
    note_id: str
    content: str
    created_at: date


def generate_id(length: int = 8) -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def error_input() -> None:
    print("\033[91m✘ Error: Invalid input. Please try again.\033[0m")


def pause(message: str = "\nPress Enter to return to the Main Menu...") -> None:
    input(message)


def prompt_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def prompt_amount(prompt: str) -> Decimal:
    while True:
        raw = input(prompt).strip()
        try:
            amount = Decimal(raw)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount.quantize(Decimal("0.01"))
        except InvalidOperation:
            error_input()


def prompt_menu_choice(min_value: int, max_value: int) -> int:
    while True:
        try:
            choice = int(input(f"Enter selection between {min_value} and {max_value}: "))
            if min_value <= choice <= max_value:
                return choice
        except ValueError:
            pass
        error_input()


def ensure_data_dir() -> None:
    DATA_DIR.mkdir(exist_ok=True)


def save_expense(expense: Expense) -> None:
    ensure_data_dir()
    file_exists = EXPENSES_FILE.exists()

    with EXPENSES_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=EXPENSE_FIELDS)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "ExpID": expense.exp_id,
            "ExpTitle": expense.title,
            "Amount": f"{expense.amount:.2f}",
            "TransDate": expense.trans_date.isoformat(),
        })


def load_expenses() -> list[Expense]:
    if not EXPENSES_FILE.exists():
        return []

    expenses: list[Expense] = []
    with EXPENSES_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                expenses.append(
                    Expense(
                        exp_id=row["ExpID"],
                        title=row["ExpTitle"],
                        amount=Decimal(row["Amount"]),
                        trans_date=date.fromisoformat(row["TransDate"]),
                    )
                )
            except (KeyError, ValueError, InvalidOperation) as exc:
                logger.warning("Skipping invalid expense row %r: %s", row, exc)
    return expenses


def save_note(note: Note) -> None:
    ensure_data_dir()
    with NOTES_FILE.open("a", encoding="utf-8") as file:
        file.write(f"[{note.note_id}] {note.created_at.isoformat()} - {note.content}\n")


def load_notes() -> list[str]:
    if not NOTES_FILE.exists():
        return []
    return NOTES_FILE.read_text(encoding="utf-8").splitlines()


def print_header(title: str) -> None:
    print("─" * 40)
    print(f"   {title}")
    print("─" * 40)


def display_menu() -> None:
    print("\nMain Menu:\n")
    for index, item in enumerate(
        ["Add new expense", "View all expenses", "Add new note", "View all notes", "Exit"],
        start=1,
    ):
        print(f"    {index}› {item}")
        print("─" * 30)


def add_expense() -> None:
    title = prompt_non_empty("Enter expense title: ").title()
    amount = prompt_amount("Enter amount (BDT): ")

    expense = Expense(
        exp_id=generate_id(),
        title=title,
        amount=amount,
        trans_date=date.today(),
    )
    save_expense(expense)
    print("\n[SUCCESS] Expense recorded successfully!")


def view_all_expenses() -> None:
    clear_screen()
    expenses = load_expenses()

    if not expenses:
        print("\n\033[93m⚠ Info: No expenses recorded yet.\033[0m")
        return

    print("═" * 60)
    print(f"{'ID':<10}  {'Expense Title':<20}  {'Amount':<10}  {'Date':<12}")
    print("─" * 60)

    total = Decimal("0.00")
    for item in expenses:
        print(f"{item.exp_id:<10}  {item.title:<20}  {item.amount:<10.2f}  {item.trans_date.isoformat():<12}")
        total += item.amount

    print("═" * 60)
    print(f"Total Records: {len(expenses)} | Overall Total: {total:.2f} BDT")
    print("═" * 60)
    pause()
    clear_screen()


def add_note() -> None:
    content = prompt_non_empty("Enter your note: ")
    note = Note(note_id=generate_id(), content=content, created_at=date.today())
    save_note(note)
    print("\n[SUCCESS] Note saved successfully!")


def view_all_notes() -> None:
    clear_screen()
    notes = load_notes()

    if not notes:
        print("\n\033[93m⚠ Info: No notes saved yet.\033[0m")
        return

    print("Saved Notes:")
    print("─" * 50)
    for note in notes:
        print(note)
    print("─" * 50)
    pause()
    clear_screen()


def run() -> None:
    actions: dict[int, Callable[[], None]] = {
        1: add_expense,
        2: view_all_expenses,
        3: add_note,
        4: view_all_notes,
    }

    while True:
        display_menu()
        choice = prompt_menu_choice(1, 5)

        if choice == 5:
            print("─" * 45)
            print(f"Thank you for using {APP_NAME}. Goodbye!")
            print("─" * 45)
            break

        clear_screen()
        actions[choice]()


def main() -> None:
    clear_screen()
    print_header(f"Welcome to {APP_NAME}")
    run()


if __name__ == "__main__":
    main()