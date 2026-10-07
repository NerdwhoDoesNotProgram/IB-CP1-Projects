# IB - Mapping Notes

"""
# MAPPING: taking an existing list, doing the same operation to every item in it, and building a brand new list out of the results — the original list is left unchanged

    * Basically running a for loop, or a funciton, to each item of the list.

# ACCUMULATOR PATTERN: a common technique where you start with an empty list, then use a for loop to add one new item to it during each pass — "accumulating" the results one at a time

# Mapping is really the accumulator pattern with one extra step: instead of just copying each item into the new list, you transform it first (like doubling a number, or making a string uppercase) before adding it

# The original list used for mapping is never changed — you always end up with two separate lists: the original, and the new transformed one

# Mapping is primarily for changing/altering a list. it always returns a new value, leaving the original data alone. It happens for every item in the list. We like using map if we accumulate, or gain, new items in the list."""

def times(number):
    return number * 2

numbers = range(1,6)

multiplied_numbers = map(times, numbers)
#                         \           \
#                Funciton name       List name
print(*list(multiplied_numbers))

new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)


siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

length = list(map(len, siblings))
print(length)
