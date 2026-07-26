students = []

# Add students
while True:
    name = input("Enter student name: ")
    course = input("Enter course: ")
    level = int(input("Enter level: "))

    student = {
        "name": name,
        "course": course,
        "level": level
    }

    students.append(student)

    choice = input("Add another student? (yes/no): ")

    if choice.lower() == "no":
        break


# Display all students
print("\nStudent List:")

for student in students:
    print("----------------")
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Level:", student["level"])


# Search for a student
print("\n--- Student Search ---")

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
    print("\nStudent not found.")