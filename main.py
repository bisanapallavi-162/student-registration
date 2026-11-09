"""Student Registration & Contact Intelligence System."""
import csv
import os
from validator import validate_record
from loader import load_contacts, save_contacts
from analytics import show_analytics

DATA_FILE = "contacts.csv"

def read_total(filename=DATA_FILE):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        return max(sum(1 for _ in csv.DictReader(file)), 0)

def display_records(records):
    if not records:
        print("No student records found.")
        return
    print("\n{:<22} {:<12} {}".format("NAME", "PHONE", "EMAIL"))
    print("-" * 65)
    for record in records:
        print("{:<22} {:<12} {}".format(record["name"], record["phone"], record["email"]))

def search_records(records):
    term = input("Enter student name or phone to search: ").strip().lower()
    matches = [r for r in records if term in r["name"].lower() or term in r["phone"]]
    display_records(matches)

def add_student(records):
    new_record = {
        "name": input("Enter student name: ").strip(),
        "phone": input("Enter 10-digit mobile number: ").strip(),
        "email": input("Enter email address: ").strip()
    }
    ok, reason = validate_record(new_record)
    if not ok:
        print("Cannot add student:", reason)
        return
    if any(r["phone"] == new_record["phone"] or r["email"].lower() == new_record["email"].lower() for r in records):
        print("Cannot add student: duplicate phone or email.")
        return
    records.append(new_record)
    save_contacts(records)
    print("Student added and saved to clean_contacts.csv.")

def main():
    if not os.path.exists(DATA_FILE):
        print("contacts.csv was not found. Keep it in the same folder as main.py.")
        return

    total = read_total()
    records, rejected = load_contacts(DATA_FILE)
    print(f"Loaded {len(records)} valid students and rejected {len(rejected)} records.")
    save_contacts(records)

    while True:
        print("\n===== STUDENT REGISTRATION MENU =====")
        print("1. View all valid students")
        print("2. Search by name or phone")
        print("3. Add a student")
        print("4. Business intelligence report")
        print("5. Show rejected records")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_records(records)
        elif choice == "2":
            search_records(records)
        elif choice == "3":
            add_student(records)
        elif choice == "4":
            show_analytics(total, records, rejected)
        elif choice == "5":
            if not rejected:
                print("No rejected records.")
            else:
                for record, reason in rejected:
                    print(f"{record} -> {reason}")
        elif choice == "6":
            print("Thank you for using the Student Registration System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
