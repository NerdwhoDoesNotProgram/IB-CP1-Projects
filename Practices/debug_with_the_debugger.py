# IB - Debug with the Debugger

# Ravager Snack Bar
import random


def assignment():
    pirate_name = input("What's your name, pirate? ")
    snack_name = input("What snack do you want? ")

    price = random.randint(2, 8)  # random price in credits
    quantity = int(input("How many would you like? ")) # Error fixed:  Runtime: ValueError. I added the int() function to convert the input string to an integer.

    total = price * quantity

    if total > 20:
        total -= 1  # Added the loyaly bonus that subtracts 1 credit off the top f the 10%% discount

    discounted_total = total - (total * 0.1)  # Error fixed: Logic error: Discount was not applied correctly. I added a line to calculate the discounted total by subtracting 10% of the total from the total, rather than just 0.2.

    tax_rate = 0.08
    total_with_tax = discounted_total + (discounted_total * tax_rate)

def regular_receipt():
    print("Hello, " + pirate_name + "! Here's your order summary:")
    print("Snack: " + snack_name) # Error fixed: Runtime error: name 'snackName' is not defined. I changed it to 'snack_name' to match the variable name used earlier in the code.
    print("Price per snack: " + str(price) + " credits") 
    print("Total before tax: " + str(discounted_total) + " credits") # Error fixed: :Logic error: Printed price instead of discounted total. I changed the variable name to 'discounted_total' to reflect the correct value. I presume that it wants the discounted total, rather than the total, as that is the number taken into account for the tax calculation.
    print("Loyalty bonus applied: 1 credit off") # Added a line to indicate that the loyalty bonus was applied to the total.
    print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # Error fixed: SytaxError: parentheses were not closed. I added the closing parentheses to the end of the line.

def fancy_receipt():
    print(f"                      RAVENGER SNACK BAR\n                    "


            f"Customer: {pirate_name}        Order #: {random.randint(1, 99)}\n"
            f"WALK-IN\n"
            f"-----------------------------------------------------------------\n"
            f"      {quantity}        {snack_name}                      = {total}"
        )


def main():
    global pirate_name, snack_name, price, quantity, total, discounted_total, total_with_tax
    assignment()
    fancy_input = ["fancy", "f", "fan" , "receipt", "receipts", "yes", "sure", "ok", "okay"]
    regular_or_fancy = input("Would you like a regular receipt or a fancy receipt? (Enter 'regular' or 'fancy'): ").lower().strip()
    if regular_or_fancy in fancy_input:
        fancy_receipt()
    else:
        regular_receipt()

main()