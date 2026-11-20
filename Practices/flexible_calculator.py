# IB Flexible Calculator

"""
Display welcome message

Define calculator function:
    Accept any number of numbers using *args
    Accept operation as a parameter
    If operation is sum:
        Return the sum of numbers
    If operation is average:
        Return the average of numbers
    If operation is max:
        Return the largest number
    If operation is min:
        Return the smallest number
    If operation is product:
        Multiply all numbers together and return result
    Otherwise:
        Return an error

Define function to collect numbers:
    Create an empty list
    Ask the user to enter numbers
    Continue asking until user types "done"
    Convert each input to a float
    Handle invalid number inputs
    Return the list of numbers

Start main program:
    Display available operations
    Ask user which operation they want
    Collect numbers
    Call calculator function using the numbers and operation
    Display the result
    Ask if user wants to calculate again
    Repeat if they say yes
    Otherwise display goodbye message
"""

def calculator(*args, operation="sum"):
    if len(args) == 0:
        return "Error: No numbers provided."

    if operation == "sum":
        return sum(args)

    elif operation == "average":
        return sum(args) / len(args)

    elif operation == "max":
        return max(args)

    elif operation == "min":
        return min(args)

    elif operation == "product":
        result = 1
        for number in args:
            result *= number
        return result

    else:
        return "Invalid operation."

def get_numbers():
    numbers = []

    print("Enter numbers (type 'done' when finished):")

    while True:
        user_input = input("Number: ").strip()

        if user_input.lower() == "done":
            break

        try:
            number = float(user_input)
            numbers.append(number)

        except ValueError:
            print("Please enter a valid number or type 'done'.")

    return numbers

def main():
    print("Welcome to the Flexible Calculator!")
    print("Available operations: sum, average, max, min, product")

    while True:
        operation = input(
            "\nWhich operation would you like to perform? "
        ).lower().strip()

        if operation not in ["sum", "average", "max", "min", "product"]:
            print("Invalid operation. Please try again.")
            continue

        numbers = get_numbers()

        if len(numbers) == 0:
            print("You didn't enter any numbers.")
            continue

        print(f"\nCalculating {operation} of: {', '.join(map(str, numbers))}")

        result = calculator(*numbers, operation=operation)

        print(f"Result: {result}")

        again = input(
            "\nWould you like to perform another calculation? (yes/no) "
        ).lower().strip()

        if again != "yes":
            break

    print("\nThank you for using the Flexible Calculator!")

main()