# IB - Debug with the Debugger

# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) # Error fixed:  Runtime: ValueError. I added the int() function to convert the input string to an integer.

total = price * quantity

discounted_total = total - 2 * 0.10

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) # Error fixed: Runtime error: name 'snackName' is not defined. I changed it to 'snack_name' to match the variable name used earlier in the code.
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(price))
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # Error fixed: SytaxError: parentheses were not closed. I added the closing parentheses to the end of the line.