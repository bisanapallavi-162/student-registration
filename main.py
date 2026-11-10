from loader import clean_contacts
from analytics import show_report

def show_contacts():
    try:
        with open("students_clean.csv", "r", encoding="utf-8") as file:
            print("\\n--- CLEAN STUDENT CONTACTS ---")
            print(file.read())
    except FileNotFoundError:
        print("No clean file found. Please clean the contacts first.")

def main():
    while True:
        print("\\n===== STUDENT REGISTRATION & CONTACT INTELLIGENCE SYSTEM =====")
        print("1. Validate and clean contacts")
        print("2. View clean contacts")
        print("3. View business report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            clean_contacts()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            show_report()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
