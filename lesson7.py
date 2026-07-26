import json
import os

# Load students from file
def load_students():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            return json.load(file)
    return []


# Save students to file
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# Add student
def add_student():
    name = input("Enter student name: ")
    course = input("Enter course: ")
    level = int(input("Enter level: "))

    student = {
        "name": name,
        "course": course,
        "level": level
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


# View students
def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\nStudent List:")

        for student in students:
            print("----------------")
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Level:", student["level"])


# Search student
def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Level:", student["level"])
            found = True

    if found == False:
        print("Student not found.")


# Load saved students
students = load_students()


# Main menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")