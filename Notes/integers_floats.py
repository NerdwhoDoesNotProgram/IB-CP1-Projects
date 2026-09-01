# IB Integers and Floats Notes

# Integer - A whole number
num = 75 # just write the number, no extra syntax required

#float - A number with a decimal point
pi = 3.1415 # Just write the number, no extra syntax required

# Arithmetic operators (+, -, *, /, **, //, %)
print(5/2)# Integer division (Only gives the integer, drops the decimal)
print(5//2) # Alwats gives you a decimal, even if it is a Zero

# Modulo/mod (modulus)
print(5%2) # Gives the remainder of a division problem
print(10%4)
print(15%5)

print((2-1)*3+4%3)
# Order of operations (P E MMD AS) (Left to right) Extra M for modulo

# assignment oporator =
print(f"Before {num}")
#num = num + 2
num += 2
print(f"After {num}")

num //= 3
print(f"Other After {num}")

num %= 4
print(f"After Mod {num}")

# Expression - Any Mathmatic equation
fav = float(input("What is your favorite number: "))

print(f"{fav**2} is {fav} squared!")
print(round(pi,3))
print(int(pi))