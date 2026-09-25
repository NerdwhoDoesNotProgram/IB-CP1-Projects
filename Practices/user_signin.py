# IB, 2nd perod - User Sign In

correct_username = "4444"
correct_passowrd = "password123" 

def get_username():
    username = input("What is your username: ")
    return username

def get_password():
    password = input("What is your password: ")
    return password

def check_login(username, password):
    if username == correct_username and password == correct_passowrd:
        return True
    else:
        return False

def main():
    username = get_username()
    password = get_password()
    if check_login(username, password):
        print("\nWelcome to the program!")
    else:
        print("\nThe username and password you entered were not recognized.")
main()