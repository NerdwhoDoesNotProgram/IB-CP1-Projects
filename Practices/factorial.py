# IB - Factorial Calculator

number = int(input("What number do you want the factorial of: "))

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

    print(" × ".join(numbers), "=", factorial)