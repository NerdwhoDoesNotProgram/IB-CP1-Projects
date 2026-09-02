# IB - Average Grade.

def find_letter_grade(average):

    if average >= 94:
        return "A"
    elif average >= 90:
        return "A-"
    elif average >= 87:
        return "B+"
    elif average >= 84:
        return "B"
    elif average >= 80:
        return "B-"
    elif average >= 77:
        return "C+"
    elif average >= 74:
        return "C"
    elif average >= 70:
        return "C-"
    elif average >= 67:
        return "D+"
    elif average >= 60:
        return "D"
    else:
        return "F"


def find_grade():

    grades = []

    for i in range(num_classes):

        while True:
            try:
                grade = input("Enter your grade for class " + str(i + 1) + ": ")
                grade = float(grade.replace("%", ""))

                if grade >= 0:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a positive grade.")

            except ValueError:
                print("Please enter a number.")

    average = sum(grades) / len(grades)
    letter_grade = find_letter_grade(average)

    print(f"Your average grade is: {round(average, 2)}% ({letter_grade})")


def valid_input():

    global num_classes

    while True:
        try:
            num_classes = int(input("How many classes do you have: "))

            if num_classes > 0:
                break
            else:
                print("Please enter a non-zero number.")

        except ValueError:
            print("Please enter a whole number.")

    find_grade()


valid_input()