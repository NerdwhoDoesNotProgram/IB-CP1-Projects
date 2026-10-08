# IB - Factorial Calculator

"""number = int(input("What number do you want the factorial of: "))

if number < 0:
    print("Factorials are only defined for non-negative integers.")
elif number == 0:
    print("0 = 1")
else:
    factorial = 1
    numbers = []

    for i in range(number, 0, -1):
        numbers.append(str(i))
        factorial *= i

    print(" × ".join(numbers), "=", factorial)"""


import math

"""
def product(number):
    return math.factorial(number)

number = int(input("What number do you want the factorial of: "))

if number < 0:
    print("Factorials are only defined for non-negative integers.")
elif number == 0:
    print("0 = 1")
else:
    numbers = range(number, 0, -1)
    numbers_string = list(map(str, numbers))

    factorial = product(number)

    print(" × ".join(numbers_string), "=", factorial)
    """

# Workspace

def product(number):
    return math.factorial(number)

class Decimal(Exception):
    pass

while True:
    try:

        number = input("What number do you want the factorial of: ").strip()


        if number.startswith("!"):
            number = int(number[1:])
        elif number.endswith("!"):
            number = int(number[:-1])
        elif  not  number.isdecimal():
            raise Decimal

        if int(number) < 0:
            print("Factorials are only defined for non-negative integers.")
        elif int(number) == 0:
           print("0 = 1")
        else:
            numbers = range(int(number), 0, -1)
            numbers_string = list(map(str, numbers))

            factorial = product(int(number))

            print(" × ".join(numbers_string), "=", factorial)

        break

    except Decimal:
         print("Please input a valid, whole number.")

    except ValueError:
        print("Number is too large to display.")

    