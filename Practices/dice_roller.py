# IB - Dice Roller Program

import random

def original_dice_roller():
    def get_dice_size():
        dice_size = input("What size dice would you like to roll? (D4, D6, D8, D10, D12, D20): ").strip().upper()

        if dice_size.startswith("D"):
            dice_size = dice_size[1:]

        if dice_size not in ["4", "6", "8", "10", "12", "20"]:
            raise ValueError("Invalid dice size. Please choose D4, D6, D8, D10, D12, or D20.")

        return int(dice_size)


    def roll_dice(dice_size, number_of_dice):
        rolls = []

        for i in range(number_of_dice):
            roll = random.randint(1, dice_size)
            rolls.append(roll)

        return rolls


    dice_size = get_dice_size()

    number_of_dice = int(input("How many dice would you like to roll? "))

    if number_of_dice <= 0:
        raise ValueError("You must roll at least one die.")

    rolls = roll_dice(dice_size, number_of_dice)

    print("You rolled:", rolls)
    print("Your rolls total to:", sum(rolls))


def dice_roller_playagain():
    def get_dice_size():
        while True:
            try:
                dice_size = input("What size dice would you like to roll? ""(D4, D6, D8, D10, D12, D20): ").strip().upper()

                if dice_size.startswith("D"):
                   dice_size = dice_size[1:]
                if dice_size not in ["1", "4", "6", "8", "10", "12", "20", "100", "5000", "999999999", "999999999999999999999999999"]:
                    raise ValueError

                return int(dice_size)

            except ValueError:
                print("Invalid dice size. Please choose ""D4, D6, D8, D10, D12, or D20.")


    def roll_dice(dice_size, number_of_dice):
        rolls = []

        for i in range(number_of_dice):
            roll = random.randint(1, dice_size)
            rolls.append(roll)

        return rolls


    while True:
        dice_size = get_dice_size()

        while True:
            try:
                number_of_dice = int(input("How many dice would you like to roll? "))

                if number_of_dice <= 0:
                    raise ValueError

                break

            except ValueError:
                print("Please enter a positive whole number.")

        rolls = roll_dice(dice_size, number_of_dice)

        if len(rolls) == 1:
            print("You rolled a", rolls[0])
        else:
            print("You rolled:", rolls)
            print("Your rolls total to:", sum(rolls))

        again = input("Would you like to roll again? (y/n): ").strip().lower()

        if again != "y" and again != "yes":
            break

    print("Thanks for playing!")


dice_roller_playagain()