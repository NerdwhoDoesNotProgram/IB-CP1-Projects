# IB - Debug with the Debugger
# Ravager Snack Bar

import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? "))
# Error fixed: Runtime error: quantity was originally stored as a string.
# I added the int() function to convert the input string to an integer.

total = price * quantity

# Advanced: Added a loyalty bonus.
# If the total before the discount is 20 credits or more,
# 1 credit is taken off in addition to the 10% discount.
loyalty_bonus = 0
if total >= 20:
    loyalty_bonus = 1
    total -= loyalty_bonus

discounted_total = total - (total * 0.10)
# Error fixed: Logic error: Discount was not applied correctly.
# I changed the calculation so that 10% of the total is subtracted
# from the total, rather than subtracting 2 * 0.10.

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)


def regular_receipt():
    print("Hello, " + pirate_name + "! Here's your order summary:")
    print("Snack: " + snack_name)
    # Error fixed: Runtime error: name 'snackName' is not defined.
    # I changed it to 'snack_name' to match the variable name used earlier in the code.

    print("Price per snack: " + str(price) + " credits")

    print("Total before tax: " + str(round(discounted_total, 2)) + " credits")
    # Error fixed: Logic error: Printed the price instead of the total.
    # I changed the variable from 'price' to 'discounted_total' because
    # the amount before tax should include the discount.

    if loyalty_bonus > 0:
        print("Loyalty bonus applied: 1 credit off")

    print("10% discount applied")
    print("Tax: " + str(round(discounted_total * tax_rate, 2)) + " credits")
    print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")


def fancy_receipt():
    print()
    print("================================================")
    print("              RAVAGER SNACK BAR")
    print("================================================")
    print("Customer: " + pirate_name)
    print("Order #: " + str(random.randint(1, 99)))
    print("WALK-IN")
    print("------------------------------------------------")
    print("Item                        Qty          Price")
    print("------------------------------------------------")

    item_total = price * quantity

    print(
        f"{snack_name:<27}"
        f"{quantity:>3}       "
        f"{item_total:>6.2f}"
    )

    print("------------------------------------------------")
    print(f"{'Subtotal:':<39}{item_total:>7.2f}")

    if loyalty_bonus > 0:
        print(f"{'Loyalty bonus:':<39}-{loyalty_bonus:>6.2f}")

    discount = total * 0.10
    print(f"{'10% discount:':<39}-{discount:>6.2f}")

    print("------------------------------------------------")
    print(f"{'Total before tax:':<39}{discounted_total:>7.2f}")

    tax = discounted_total * tax_rate
    print(f"{'Tax (8%):':<39}{tax:>7.2f}")

    print("------------------------------------------------")
    print(f"{'TOTAL:':<39}{total_with_tax:>7.2f}")
    print("================================================")
    print("          Thank you for your business!")
    print("================================================")


def main():
    fancy_input = [
        "fancy", "f", "fan", "receipt",
        "receipts", "yes", "sure", "ok", "okay"
    ]

    regular_or_fancy = input(
        "Would you like a regular receipt or a fancy receipt? "
        "(Enter 'regular' or 'fancy'): "
    ).lower().strip()

    if regular_or_fancy in fancy_input:
        fancy_receipt()
    else:
        regular_receipt()


main()