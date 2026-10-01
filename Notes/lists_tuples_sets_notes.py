# IB Lists, Tuples, and Sets Notes


# List []

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
# variable name, Bracket, proper data type in quotation, comma separating htem.
length = len(siblings)
print(f"My older sister is {siblings[1]}")
# Variable name, and within brackets, put the index number
print(*siblings)
# * is the unpacking operator, which removes the list foratting from the list
print(f'The youngest is {siblings[-1]}')
siblings.append("Jayshree")
siblings.insert(3, "Vienna")
siblings.extend(["Joe", "Israel", "Zee"])
siblings.remove("Vienna")
siblings.pop(0)
print(*siblings)

# delete list_name[index]

#_______________________________________________________________________________________________
#  Tuples ()

subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Studies", 'US 1', "US 2", "World Civ", "World Geography", "CCA Business")
print()
print(subjects[0])
print(*subjects)

# Tules are Immutable

#_______________________________________________________________________________________________

# Sets {}

visited_locaitons = {"Texa", 'Ohio', 'Minnesota', 'Virginia', 'D.C.', 'Utah', 'California', 'Nevada'}
print()
visited_locaitons.add("Idaho")
print(len(visited_locaitons))
print(*visited_locaitons)
visited_locaitons.update({"Montana", "Arizona", "Oklahoma", "New Mexico"})
print(*visited_locaitons)
visited_locaitons.remove("Arizona")
print(*visited_locaitons)


# Can convert between types. (Creates a new variable)
# set(variable_name)
# list(variable_name)
# tuple(variable_name)

# Can convert list to set and back to remove duplicates