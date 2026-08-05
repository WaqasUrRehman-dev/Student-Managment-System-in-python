import json
import os

students = []

def show_header():
    print("===============================")
    print("Welcome to Student Management System")
    print("===============================")

def load_students():
    global students
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            students = json.load(file)
    else:
        students = []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students,file,indent=4)

def find_student_by_cnic(cnic):
    for student in students:
        if cnic == student['cnic']:
            return student
    return None

def display_student(student):
    print(f"Name : {student['name']}")
    print(f"Age : {student['age']}")
    print(f"Email : {student['email']}")
    print(f"Cnic : {student['cnic']}")
    print()

def validate_name():
    
    while True:

        name = input("Enter your name: ")

        if name.strip() == "":

            print("Name is required")
            continue

        else:
            return name

def validate_age():

    while True:

        age = input("Enter your age: ")

        if age.strip() == "":

            print("Age is required")
            continue

        elif age.isdigit() != True:

            print("Age must contain numbers only")
            continue

        elif int(age) <= 0:

            print("Age must be greater than 0")
            continue

        elif int(age) > 120:

            print("Age limit must be less than 120")
            continue

        else:

            return int(age)


def validate_email():
    
    while True:

        email = input("Enter your email address: ")

        if email.strip() == "":

            print("Email is required")
            continue

        elif email.count("@") != 1 or email.count(".") < 1:

            print("Email must contain @ and .")
            continue
        
        else:

            return email


def validate_cnic():
    
    while True:

        cnic = input("Enter Your Cnic: ")

        clean_cnic = cnic.replace("-","")

        if clean_cnic.strip() == "":

            print("Cnic is required")
            continue

        elif clean_cnic.isdigit() != True:

            print("Cnic must contain numbers only")
            continue

        elif len(clean_cnic) != 13:

            print("Cnic length should be 13 digits")
            continue

        else:
            
            return cnic

def add_student():
    name = validate_name()
    age = validate_age()
    email = validate_email()
    cnic = validate_cnic()
    existing_student = find_student_by_cnic(cnic)
    if existing_student:
        print("Cnic is Already Exist.")
        return

    student = {
        "name": name,
        "age": age,
        "email": email,
        "cnic": cnic
    }

    students.append(student)

    save_students()

    print(f"{name} Student added Successfully")


def view_students():

    if not students:
        print("No Student added yet.")
        return
    for i, data in enumerate(students, start=1):
        print("==============================")
        print(f"========= Student #{i} =========")
        print("==============================")
        display_student(data)

def search_student():

    if not students:
        print("No student added yet.")
        return
    user_cnic = validate_cnic()
    student = find_student_by_cnic(user_cnic)
    if student:
        display_student(student)
    else:
        print("No Student Found.")
        print()


def update_student():
    updated_student = False
    if not students:
        print("No student added yet.")
        return
    user_cnic = validate_cnic()
    student = find_student_by_cnic(user_cnic)
    if student:
        display_student(student)

        print("What do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Email")
        print("4. Cnic")

        option = input("Enter Option: ")

        if option == "1":
            student["name"] = validate_name() 
            updated_student = True
        elif option == "2":
            student["age"] = validate_age()
            updated_student = True
        elif option == "3":
            student["email"] = validate_email()
            updated_student = True
        elif option == "4":
            update_cnic = validate_cnic()
            existing_student = find_student_by_cnic(update_cnic)
            if student is existing_student or not existing_student:
                student["cnic"] = update_cnic
                updated_student = True
            else:
                print("Cnic is Already Exist.")
        else:
            print("Invalid Input")

        if updated_student:
            save_students()
            print("Student Updated Successfully")
    else:
        print("No Student Found.")
        print()
                

def delete_student():

    if not students:
        print("No Student added yet.")
        return
    user_cnic = validate_cnic()
    student = find_student_by_cnic(user_cnic)
    if student:
        display_student(student)

        print("Are you sure, you want to delete this student")
        print("1. Yes")
        print("2. No")

        option = input("Enter Option: ")

        if option == "1":
            students.remove(student)
            save_students()
            print("Student Deleted Successfully")
        elif option == "2":
            print("Deletion Cancelled.")

    else:
        print("No Student Found.")
        print()

def menu():

    load_students()
    show_header()
    
    while True:

        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        option = input("Enter option: ")

        if option == "1":
            add_student()
        elif option == "2":
            view_students()
        elif option == "3":
            search_student()
        elif option == "4":
            update_student()
        elif option == "5":
            delete_student()
        elif option == "6":
            break
        else:
            print("Invalid input")


menu()