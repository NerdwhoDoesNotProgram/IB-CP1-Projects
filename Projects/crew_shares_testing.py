# IB, 2nd period - Crew Shares TESTING

import random

def pirates():
    number_of_pirates = int(input("How many pirates: "))

    while number_of_pirates < 3:
        print("There must be at least 3 pirates: Yondu, Peter, and at least one crew member.")
        number_of_pirates = int(input("How many pirates: "))

    crew_names = []

    enter_names = input("Do you want to enter the crew member names? (yes/no): ")

    if enter_names.lower() == "yes":
        for number in range(number_of_pirates - 2):
            name = input("Enter crew member name: ")
            crew_names.append(name)

    return number_of_pirates, crew_names


def yondu(remaining_units):
    yondu_share = round(remaining_units * 0.13, 2)
    remaining_units -= yondu_share

    return yondu_share, remaining_units


def peter(remaining_units):
    peter_share = round(remaining_units * 0.11, 2)
    remaining_units -= peter_share

    return peter_share, remaining_units


def crew(remaining_units, number_of_pirates):
    crew_share = round(remaining_units / number_of_pirates, 2)

    return crew_share


def main():
    number_of_pirates, crew_names = pirates()

    starting_units = random.randint(500, 5000)
    remaining_units = starting_units

    number_of_crew = number_of_pirates - 2
    units_given_early = number_of_crew * 3
    remaining_units -= units_given_early

    yondu_share, remaining_units = yondu(remaining_units)

    peter_share, remaining_units = peter(remaining_units)

    crew_share = crew(remaining_units, number_of_pirates)

    yondu_total = round(yondu_share + crew_share, 2)
    peter_total = round(peter_share + crew_share, 2)
    individual_crew_share = round(crew_share + 3, 2)

    print()
    print(f"Units found: {starting_units}")
    print(f"Yondu's share: {yondu_total:.2f}")
    print(f"Peter's share: {peter_total:.2f}")

    if len(crew_names) > 0:
        for name in crew_names:
            print(f"{name}'s share: {individual_crew_share:.2f}")
    else:
        print(f"Crew's share: {individual_crew_share:.2f}")


main()