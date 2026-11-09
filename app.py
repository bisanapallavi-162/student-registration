"""Student Registration & Contact Intelligence System.
A simple command-line project using Python and CSV file storage.
"""

import csv
import os
from datetime import datetime

DATA_FILE = "students.csv"
FIELDS = [
    "student_id", "name", "email", "phone",
    "course", "city", "registered_on"
]


def ensure_data_file():
    """Create the CSV file and its headings when needed."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writeheader()


def get_students():
    ensure_data_file()
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_students(students):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def display_student(student):
    print("-" * 42)
    for field in FIELDS:
        print(f"{field.replace('_', ' ').title()}: {student.get(field, '')}")
    print("-" * 42)


def register_student():
    students = get_students()
    print("\n--- Student Registration ---")
    student_id = input("Student ID: ").strip()

    if not student_id:
        print("Student ID is required.")
        return
    if any(s["student_id"].lower() == student_id.lower() for s in students):
        print("That student ID already exists.")
        return

    name = input("Full name: ").strip()
    email = input("Email address: ").strip()
    phone = input("Phone number: ").strip()
    course = input("Course: ").strip()
    city = input("City: ").strip()

    if not all([name, email, phone, course, city]):
        print("Please fill in all fields.")
        return
    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        print("Please enter a valid email address.")
        return

    if any(s["email"].lower() == email.lower() for s in students):
        print("This email address is already registered.")
        return

    students.append({
        "student_id": student_id,
        "name": name,
        "email": email,
        "phone": phone,
        "course": course,
        "city": city,
        "registered_on": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_students(students)
    print("Student registered successfully.")


def view_all_students():
    students = get_students()
    print("\n--- All Student Records ---")
    if not students:
        print("No student records are available.")
        return
    for student in students:
        display_student(student)
    print(f"Total students: {len(students)}")


def search_contact():
    """Search student contact information by ID, name, email or phone."""
    students = get_students()
    term = input("Enter ID, name, email or phone to search: ").strip().lower()

    if not term:
        print("Please enter a search term.")
        return

    matches = [
        student for student in students
        if any(term in student[field].lower()
               for field in ["student_id", "name", "email", "phone"])
    ]

    if not matches:
        print("No matching student/contact found.")
        return

    print(f"\nFound {len(matches)} matching record(s):")
    for student in matches:
        display_student(student)


def update_student():
    students = get_students()
    student_id = input("Enter the student ID to update: ").strip().lower()

    for student in students:
        if student["student_id"].lower() == student_id:
            print("Press Enter to keep the existing value.")
            for field in ["name", "email", "phone", "course", "city"]:
                new_value = input(
                    f"{field.replace('_', ' ').title()} "
                    f"({student[field]}): "
                ).strip()
                if new_value:
                    student[field] = new_value
            save_students(students)
            print("Student information updated.")
            return

    print("Student ID not found.")


def delete_student():
    students = get_students()
    student_id = input("Enter the student ID to delete: ").strip().lower()
    remaining = [
        student for student in students
        if student["student_id"].lower() != student_id
    ]

    if len(remaining) == len(students):
        print("Student ID not found.")
    else:
        save_students(remaining)
        print("Student record deleted.")


def show_menu():
    print("\n==============================================")
    print(" STUDENT REGISTRATION & CONTACT INTELLIGENCE")
    print("==============================================")
    print("1. Register a student")
    print("2. View all students")
    print("3. Search student/contact")
    print("4. Update student details")
    print("5. Delete student record")
    print("6. Exit")


def main():
    ensure_data_file()
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the project.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
