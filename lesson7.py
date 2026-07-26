students = []


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

    print("Student added successfully!")


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


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")