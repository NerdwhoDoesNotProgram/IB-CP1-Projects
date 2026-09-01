# IB - Average Grade.

def find_grade():
    
    total = 0

    for i in range(num_classes):
        grade = input("Enter your grade for class " + str(i + 1) + ": ")
        grade = float(grade.replace("%", ""))
        total += grade

    global average
    average = total / num_classes
    print(f"Your average grade is: {round(average, 2)}%")


def valid_input():
    global num_classes
    num_classes = int(input("How many classes do you have: "))


    while num_classes == 0:
            num_classes= int(input("Please input a Non-zero number: "))
            find_grade()
    else:
        find_grade()


valid_input()