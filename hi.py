students = []


# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    # Marks Validation
    if marks < 0 or marks > 100:
        print("Invalid Marks! Marks must be between 0 and 100.")
        return

    # Automatic Grading
    if marks >= 80:
        grade = "1st Division"
    elif marks >= 60:
        grade = "2nd Division"
    elif marks >= 40:
        grade = "3rd Division"
    else:
        grade = "Fail"

    # Student Dictionary
    student = {
        "Student ID": student_id,
        "Student Name": name,
        "Age": age,
        "Department": department,
        "Marks": marks,
        "Grade": grade
    }

    # Add dictionary to list
    students.append(student)

    print("Student Added Successfully!")


# View All Students
def view_students():
    if len(students) == 0:
        print("No Student Records Available.")
        return

    for student in students:
        print(student)


# Search Student by ID or Name
def search_student():
    search_value = input("Enter Student ID or Name: ")

    for student in students:

        if (student["Student ID"] == search_value or
                student["Student Name"].lower() == search_value.lower()):

            print("Student Found:")
            print(student)
            return

    print("Student Not Found.")


# Delete Student
def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    for student in students:

        if student["Student ID"] == student_id:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found.")


# Main Menu
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Exited.")
        break

    else:
        print("Invalid Choice! Please enter 1 to 5.")