# IB, 2nd perod - User Sign In

# Aspire?
# Want a sign up
#
#
#
#
#
#
#
"""
from plyer import notification

notification.notify(
    title="Python Alert",
    message="This is a native computer notification!",
    app_name="My Python Script",
    timeout=10 # Duration in seconds the notification stays on screen
)
"""
#
import random, time, sys

import tkinter as tk
from tkinter import messagebox

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
        root = tk.Tk()
        root.withdraw()

        messagebox.showinfo(
            "Aspire Verification",
            f"Your verification code is: {code}"
        )

        root.destroy()

    except tk.TclError:
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

def main():
    username = get_username()
    password = get_password()
    code = generate_code()

    if check_login(username, password):
        code = generate_code()
        show_code(code)

        if verify_code(code):
            if USERS[username]['type'] == 'student' or USERS[username]['type'] == 'Student':
                print(f"\nWelcome, {USERS[username]['name']}\n") 
                print(f"{USERS[username]['grades']}")
                print(f"Your grade level is: {USERS[username]['grade']}")

            elif USERS[username]['type'] == 'teacher':
                print(f"\nWelcome, {USERS[username]['name']}\n")

            elif USERS[username]['type'] == 'admin':
                print(f"\nWelcome, {USERS[username]['name']}\n")
        else:
            print("\nToo many incorrect attempts.")

    else:
        print("\nThe username and password you entered were not recognized.")


main()