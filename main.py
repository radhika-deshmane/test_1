# Student Management System
# This program allows users to add, view, search,
# update, and delete student records.

students = []

# Function to add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.\n")


# Function to display all students
def view_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\nStudent Records:")
    print("-" * 40)

    for student in students:
        print(f"Name  : {student['name']}")
        print(f"Roll  : {student['roll']}")
        print(f"Marks : {student['marks']}")
        print("-" * 40)


# Function to search student
def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            print(f"Name  : {student['name']}")
            print(f"Roll  : {student['roll']}")
            print(f"Marks : {student['marks']}\n")
            return

    print("Student not found.\n")


# Function to update student
def update_student():
    roll = input("Enter roll number to update: ")

    for student in students:
        if student["roll"] == roll:
            print("Enter new details:")

            student["name"] = input("New name: ")
            student["marks"] = float(input("New marks: "))

            print("Student updated successfully.\n")
            return

    print("Student not found.\n")


# Function to delete student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully.\n")
            return

    print("Student not found.\n")


# Main menu function
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.\n")


# Program starts here
menu()