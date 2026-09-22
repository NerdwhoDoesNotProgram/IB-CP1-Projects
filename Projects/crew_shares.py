# IB, 2nd period - Crew Shares

import random

def crew_members():
    number_in_crew = int(input("How many crew members: "))

    while number_in_crew < 1 or number_in_crew > 100:
        print("There must be at least one crew member and no more than 100 crew members.")
        number_in_crew = int(input("How many crew members: "))

    crew_names = []

    enter_names = input("Do you want to enter the crew member names? (yes/no): ")

    if enter_names.lower() == "yes":
        for number in range(number_in_crew):
            name = input("Enter crew member name: ")
            crew_names.append(name)

    return number_in_crew, crew_names

def yondu(remaining_units):
    yondu_share = round(remaining_units * 0.13, 2)
    remaining_units -= yondu_share

    return yondu_share, remaining_units

def peter(remaining_units):
    peter_share = round(remaining_units * 0.11, 2)
    remaining_units -= peter_share

    return peter_share, remaining_units

def crew(remaining_units, number_in_crew):
    crew_share = round(remaining_units / (number_in_crew + 2), 2)
    return crew_share

def main():
    number_in_crew, crew_names = crew_members()

    starting_units = random.randint(500, 5000)
    remaining_units = starting_units

    units_given_early = number_in_crew * 3
    remaining_units -= units_given_early

    yondu_share, remaining_units = yondu(remaining_units)

    peter_share, remaining_units = peter(remaining_units)

    crew_share = crew(remaining_units, number_in_crew)

    yondu_total = round(yondu_share + crew_share, 2)
    peter_total = round(peter_share + crew_share, 2)
    individual_crew_total = round(crew_share, 2)

    print()
    print(f"Units found: {starting_units}")
    print(f"Yondu's share: {yondu_total:.2f}")
    print(f"Peter's share: {peter_total:.2f}")

    if len(crew_names) > 0:
        for name in crew_names:
            print(f"{name}'s share: {individual_crew_total:.2f}")
    else:
        print(f"Crew's share: {individual_crew_total:.2f}")

main()
