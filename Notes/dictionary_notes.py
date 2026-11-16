# IB - Dictionary notes

# Collection of key and value pairs

car = {
    # Key  :  Value
    "make" : "Jeep",
    "model" : "Wrangler",
    "color" : "silver",
    "year" : 2023
}
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

car.pop("color")
print(car.items())

keys = list(car.keys())

for key in keys:
    print(f"{key} is {car[key]}")

values = list(car.values())
print(values)

print(len(car))


avatar = {
    'water' : {
        "katara" : "Water bender",
        'Sokka' : 'Leader, sword master'
    },
    "Earth" : {
        "Toph" : "Earth bender",
        "Suki" : "Warrior from Kyoshi Island",
        "Cabbage Merchant" : "My CABBAGES!!!!"
    },
    "Air" : {
        "Aang" :"Air bender, the Avatar"
    },
    "Fire" : {
        "Zuko" : "Fire bender",
        "Iroh" : "Fire bender, dragon of the west",
        "Azula" : "Fire bender"
    }
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Cabbage Merchant"))

"""
# What is a dictionary, and how is it different from a list?

# What is a key-value pair?

# How do you create a dictionary? How do you create an empty one?

# How do you get a value out of a dictionary? What happens if the key doesn't exist?

# How do you add, change, and delete a key-value pair?

# What are three ways to loop through a dictionary?

# What happens if you add a key that already exists?

# What can be used as a key? What can be used as a value?

# What is a nested dictionary, and how do you access a value inside one?

"""

# Key Concepts

"""
# Dictionary: a collection of key-value pairs. You look things up by key, like looking up a word in a real dictionary.

# Key: the label used to find a value. Keys must be unique and unchangeable (strings, numbers, and tuples work; lists do not).

# Value: the data stored with a key. It can be any type, including a list or another dictionary.

# Lists vs. dictionaries: a list finds items by position (nums[0]). A dictionary finds items by key (student["name"]).

# Duplicate keys: a key can only exist once. Assigning to an existing key replaces its value.

# KeyError: the error you get when you use d[key] and the key isn't there. d.get(key) avoids it.

# Nested dictionary: a dictionary stored as a value inside another dictionary. Use one pair of brackets per level: people["Sam"]["age"].

# Reference type: a dictionary is a complex (reference) data type, not a simple primitive like an int or a bool
"""