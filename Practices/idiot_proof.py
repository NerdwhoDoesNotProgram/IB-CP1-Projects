# IB, 2nd period - Idiot Proof Assignment

def get_name():
    while True:
        try:
            # name only contains letters and spaces
            if not full_name.replace(" ", "").isalpha():
                raise ValueError
            
            first_name = input("What is your first name: ").strip().title()
            last_name = input("What is your last name: ").strip().title()
            first_separated = first_name.split()
            fixed = "".join(first_separated)
            last_separated = last_name.split()
            last_fixed = "".join(last_separated)
            full_name = fixed.title() + " " + last_fixed.title()

            name = full_name.title()

            return name

        except ValueError:
            print("That's not a valid name, try again.")


def get_phone():
    while True:
        try:
            phone = input("What is your phone number? ").strip()

            # Remove common formatting characters
            phone = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")

            # Make sure the phone number is exactly 10 digits
            if len(phone) != 10 or not phone.isnumeric():
                raise ValueError

            # Format as 000 000 0000
            phone = phone[:3] + " " + phone[3:6] + " " + phone[6:]

            return phone

        except ValueError:
            print("That's not a valid phone number, try again.")


def get_gpa():
    while True:
        try:
            gpa = float(input("What is your GPA? ").strip())

            # Make sure GPA is within a normal 0.0–4.0 range, unless you live in texas, then this would be wrong)
            if gpa < 0 or gpa > 4:
                raise ValueError

            gpa = round(gpa, 1)

            return gpa

        except ValueError:
            print("That's not a valid GPA, try again.")


name = get_name()
phone = get_phone()
gpa = get_gpa()

print()
print("name:", name)
print("phone:", phone)
print("GPA:", gpa)