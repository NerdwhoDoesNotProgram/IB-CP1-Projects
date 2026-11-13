# IB - Combat Program

"""
GET  user class
SET list of user stats from possible numbers by class
DISPLAY 
"""

"""
def user_stats():
    pass

def player_char(name, user_stats):
    pass

def class_stats():
    user_stats = []
    return user_stats

def intro():
    while True:
        print("Welcome to training! First I need to know some things about you!")

        name = input("What is your name: ")

        fighter_class = input("What class of fighter are you: ")

        class_stats(fighter_class)

        return name, fighter_class

def instructions():
    pass

def user_turn():
    pass

def combat():
    pass

def monster_attack():
    pass

def damage():
    pass

def health():
    pass

def win():
    pass


def run_game():
    intro()
"""


import random

def class_stats(fighter_class):
    if fighter_class == "1":
        user_stats = {
        "health": 30,
        "defense": 14,
        "attack_bonus": 3,
        "damage_bonus": 4
        }
    elif fighter_class == "2":
        user_stats = {
        "health": 24,
        "defense": 12,
        "attack_bonus": 4,
        "damage_bonus": 5
        }
    elif fighter_class == "3":
        user_stats = {
        "health": 27,
        "defense": 15,
        "attack_bonus": 4,
        "damage_bonus": 3
        }

    return user_stats

def player_char(name, user_stats):
    player = {
    "name": name,
    "health": user_stats["health"],
    "defense": user_stats["defense"],
    "attack_bonus": user_stats["attack_bonus"],
    "damage_bonus": user_stats["damage_bonus"],
    "potions": 2,
    "defending": False
    }

    return player

def intro():
    print("Welcome to training! First I need to know some things about you!")

    name = input("What is your name? ")

    while True:
        print("What class of fighter are you?")
        print("1. Fighter")
        print("2. Mage")
        print("3. Rogue")

        fighter_class = input("Choose 1, 2, or 3: ")

        if fighter_class in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please try again.")

    user_stats = class_stats(fighter_class)
    player = player_char(name, user_stats)

    print("\nGreat, here are your stats!")
    print("Health:", player["health"])
    print("Defense:", player["defense"])
    print("Attack: D20 +", player["attack_bonus"])
    print("Damage: D8 +", player["damage_bonus"])

    return player

def instructions():
    print("\nCombat Instructions:")
    print("1. Normal Attack - Standard damage")
    print("2. Wild Attack - More damage, but you take damage")
    print("3. Drink a Healing Potion - Regain 9 health")
    print("4. Defend - Increase defense against the next attack")
    print("5. Flee - Attempt to escape the battle")

def user_turn(player, monster):
    player["defending"] = False

    while True:
        print("\nWhat would you like to do?")
        print("1. Normal Attack")
        print("2. Wild Attack")
        print("3. Drink a Healing Potion")
        print("4. Defend")
        print("5. Flee")

        choice = input("Choose an action: ")

        if choice == "1":
            attack_roll = random.randint(1, 20) + player["attack_bonus"]

            if attack_roll >= monster["defense"]:
                damage = random.randint(1, 8) + player["damage_bonus"]
                monster["health"] -= damage

                print("You hit!")
                print("You dealt", damage, "damage.")
                print(monster["name"], "now has",
                    max(0, monster["health"]), "health.")
            else:
                print("You missed!")

            return "continue"

        elif choice == "2":
            attack_roll = random.randint(1, 20) + player["attack_bonus"]

            if attack_roll >= monster["defense"]:
                damage = (random.randint(1, 8) + player["damage_bonus"]) * 2
                monster["health"] -= damage

                player["health"] -= 4

                print("You unleash a wild attack!")
                print("You dealt", damage, "damage.")
                print("You also took 4 damage!")
                print("Your health:", max(0, player["health"]))
                print(monster["name"], "now has",
                    max(0, monster["health"]), "health.")
            else:
                player["health"] -= 4

                print("Your wild attack missed!")
                print("You still took 4 damage.")
                print("Your health:", max(0, player["health"]))

            return "continue"

        elif choice == "3":
            if player["potions"] > 0:
                player["health"] += 9
                player["potions"] -= 1

                print("You drank a healing potion!")
                print("You regained 9 health.")
                print("Your health:", player["health"])
                print("Potions remaining:", player["potions"])

                return "continue"
            else:
                print("You have no healing potions left!")

        elif choice == "4":
            player["defending"] = True

            print("You prepare to defend yourself!")
            print("Your defense will increase for the next attack.")

            return "continue"

        elif choice == "5":
            flee_roll = random.randint(1, 20)

            if flee_roll >= 10:
                print("You successfully escaped!")
                return "flee"
            else:
                print("You failed to escape!")
                return "continue"

        else:
            print("Invalid choice. Please choose 1-5.")

def monster_attack(player, monster):
    print("\nThe", monster["name"], "attacks!")

    attack_roll = random.randint(1, 20) + monster["attack_bonus"]

    defense = player["defense"]

    if player["defending"]:
        defense += 4
        print("Your defense increased to", defense, "!")

    if attack_roll >= defense:
        damage = random.randint(1, 8) + monster["damage_bonus"]
        player["health"] -= damage

        print("The monster hit you!")
        print("You took", damage, "damage.")
        print("Your health:", max(0, player["health"]))
    else:
        print("The monster missed!")

    player["defending"] = False

def combat(player):
    monster = {
    "name": "Dire Wolf",
    "health": 36,
    "defense": 13,
    "attack_bonus": 3,
    "damage_bonus": 2
    }

    print("\nYou are being attacked by a", monster["name"], "!")

    first_turn = random.choice(["player", "monster"])

    if first_turn == "player":
        print("You move first!")
    else:
        print("The monster moves first!")

    while player["health"] > 0 and monster["health"] > 0:

        if first_turn == "player":
            result = user_turn(player, monster)

            if result == "flee":
                return

            if player["health"] <= 0 or monster["health"] <= 0:
                break

            monster_attack(player, monster)

        else:
            monster_attack(player, monster)

            if player["health"] <= 0 or monster["health"] <= 0:
                break

            result = user_turn(player, monster)

            if result == "flee":
                return

        first_turn = "player"

    if player["health"] <= 0:
        print("\nYou have been defeated!")
        print("Better luck next time!")

    elif monster["health"] <= 0:
        print("\nCongratulations!")
        print("You defeated the", monster["name"], "!")
        print("You have", player["health"], "health remaining.")

def run_game():
    player = intro()
    instructions()
    combat(player)

run_game()