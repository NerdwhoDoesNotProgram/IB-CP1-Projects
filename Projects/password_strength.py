# IB - Password Strength Checker

def length(password):
    return len(password) >= 8


def uppercase(password):
    for char in password:
        if 65 <= ord(char) <= 90:
            return True
    return False


def lowercase(password):
    for char in password:
        if 97 <= ord(char) <= 122:
            return True
    return False


def numbers(password):
    for char in password:
        if 48 <= ord(char) <= 57:
            return True
    return False


def special_char(password):
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in password:
        if char in special_chars:
            return True
    return False


def main():
    password = input("Enter a password: ")
    points = 0

    length_point = length(password)
    upper_point = uppercase(password)
    lower_point = lowercase(password)
    numbers_point = numbers(password)
    special_point = special_char(password)

    print("\nPassword strength assessment:")
    print("Length (8+ characters):", "Yes" if length_point else "No")
    print("Contains uppercase:", "Yes" if upper_point else "No")
    print("Contains lowercase:", "Yes" if lower_point else "No")
    print("Contains numbers:", "Yes" if numbers_point else "No")
    print("Contains special characters:", "Yes" if special_point else "No")

    if length_point:
        points += 1
    if upper_point:
        points += 1
    if lower_point:
        points += 1
    if numbers_point:
        points += 1
    if special_point:
        points += 1

    if points <= 2:
        strength = "Weak"
    elif points == 3:
        strength = "Moderate"
    elif points == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\nStrength score:" + str(points) + "/5")
    print("Password strength:" + str(strength))


main()
