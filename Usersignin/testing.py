# IB, 2nd perod - User Sign In


import random, warnings # time, sys

from plyer import notification
warnings.filterwarnings("ignore", category=UserWarning)


from storage import USERS


def get_username():
    username = input("What is your username: ")
    return username

def get_password():
    password = input("What is your password: ")
    return password

def check_login(username, password):
    if username in USERS and USERS[username]["password"] == password:        
        return True
    else:
        return False

def generate_code():
    code = random.randint(100000, 999999)
    return code

def show_code(code):
    try:
        notification.notify(
            title = "Aspire Verification",
            message = f"Your verification code is: {code}",
            app_name = "Aspire",
        )

    except Exception: #(NotImplementedError, Exception) as e:
        print(f"\nYour verification code is: {code}")

def verify_code(code):
    attempts = 0

    while attempts < 3:
        entered_code = input("Enter your verification code: ")

        if entered_code == str(code):
            return True

        attempts += 1
        print("Incorrect verification code.")

    return False

def check_new_username(username):
    if username in USERS:
        return False
    else:
        return True

def get_new_username():
    while True:
        username = input("Enter your 4-digit student ID: ")

        if len(username) == 4 and username.isdigit():
            if check_new_username(username):
                return username
            else:
                print("That student ID is already in use.")
        else:
            print("Student ID must be exactly 4 digits.")

def get_new_name():
    name = input("Enter your name: ")
    return name

def get_new_grade():
    while True:
        grade = input("Enter your grade level (9-12): ")

        if grade in ["9", "10", "11", "12"]:
            return int(grade)
        else:
            print("Please enter a grade level from 9 to 12.")

def get_new_password():
    while True:
        password = input("Create a password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            return password
        else:
            print("The passwords do not match. Please try again.")

def new_user():
    username = get_new_username()
    name = get_new_name()
    grade = get_new_grade()
    password = get_new_password()
    grades = generate_grades()
    
    USERS[username] = {
        "name": name,
        "grade": grade,
        "password": password,
        "type": "student",
        "grades": grades
    }

    print("\nYour Aspire account has been created!")
    print(f"Your student ID is: {username}")
    print("\nYour starting grades are:")
    print(grades)

def generate_grades():
    grades = {
        "CS 1400": random.randint(85, 100),
        "Math": random.randint(85, 100),
        "Health": random.randint(85, 100),
        "Chemistry": random.randint(85, 100),
        "Speech": random.randint(85, 100),
        "English": random.randint(85, 100)
    }

    return grades

def view_grades(username):
    print("\nYour Grades")
    print("-----------")

    grades = USERS[username]["grades"]

    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

def view_student_info(username):
    print("\nStudent Information")
    print("-------------------")
    print(f"Name: {USERS[username]['name']}")
    print(f"Student ID: {username}")
    print(f"Grade Level: {USERS[username]['grade']}")

def student_portal(username):
    while True:
        print("\nAspire Student Portal")
        print("---------------------")
        print("1. View Grades")
        print("2. View Student Information")
        print("3. Sign Out")

        choice = input("Choose an option: ")

        if choice == "1":
            view_grades(username)

        elif choice == "2":
            view_student_info(username)

        elif choice == "3":
            print("\nYou have been signed out.")
            break

        else:
            print("\nInvalid choice. Please try again.")

def view_students():
    print("\nStudents")
    print("--------")

    for username, user in USERS.items():
        if user["type"] == "student" or user["type"] == "Student":
            print(f"{username}: {user['name']} - Grade {user['grade']}")

def teacher_portal(username):
    while True:
        print("\nAspire Teacher Portal")
        print("---------------------")
        print("1. View Students")
        print("2. Sign Out")

        choice = input("Choose an option: ")

        if choice == "1":
            view_students()

        elif choice == "2":
            print("\nYou have been signed out.")
            break

        else:
            print("\nInvalid choice. Please try again.")

def view_all_users():
    print("\nAll Users")
    print("---------")

    print("\nStudents:")
    for username, user in USERS.items():
        if user["type"] == "student" or user["type"] == "Student":
            print(f"{username}: {user['name']} - Grade {user['grade']}")

    print("\nTeachers:")
    for username, user in USERS.items():
        if user["type"] == "teacher":
            print(f"{username}: {user['name']}")

    print("\nAdmins:")
    for username, user in USERS.items():
        if user["type"] == "admin":
            print(f"{username}: {user['name']}")

def admin_portal(username):
    while True:
        print("\nAspire Admin Portal")
        print("-------------------")
        print("1. View All Users")
        print("2. Sign Out")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_users()

        elif choice == "2":
            print("\nYou have been signed out.")
            break

        else:
            print("\nInvalid choice. Please try again.")

def login():
    username = get_username()
    password = get_password()

    if check_login(username, password):
        code = generate_code()
        show_code(code)

        if verify_code(code):
            if USERS[username]['type'] == 'student' or USERS[username]['type'] == 'Student':
                print(f"\nWelcome, {USERS[username]['name']}\n")
                student_portal(username)

            elif USERS[username]["type"] == "teacher":
                print(f"\nWelcome, {USERS[username]['name']}\n")
                teacher_portal(username)

            elif USERS[username]["type"] == "admin":
                print(f"\nWelcome, {USERS[username]['name']}\n")
                admin_portal(username)

        else:
            print("\nToo many incorrect attempts.")

    else:
        print("\nThe username and password you entered were not recognized.")


def main():
    while True:
        print("\nWelcome to Aspire")
        print("1. Log in")
        print("2. Create an account")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            login()

        elif choice == "2":
            new_user()

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

main()