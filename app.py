students = []

def add_student():
    name = input("Student Name: ")
    roll = input("Roll No: ")
    contact = input("Contact: ")
    students.append({"name": name, "roll": roll, "contact": contact})
    print("Student Added Successfully!")

def view_students():
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Contact: {s['contact']}")

while True:
    print("\n1. Add Student 2. View Students 3. Exit")
    ch = input("Choose: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        break
