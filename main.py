def show_header():
    print("===============================")
    print("Welcome to Student Management System")
    print("===============================")

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


def view_students():
    pass

def search_student():
    pass

def update_student():
    pass

def delete_student():
    pass

def exit_app():
    pass

def menu():

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

print("Main Branch Update")
print("Learning Git diff")
print("Learning Git Revert")