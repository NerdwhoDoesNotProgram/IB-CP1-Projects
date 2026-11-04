# IB - Caesar_Cipher.py

"""def encode():
    print("encode")

def decode():
    print("decode")

def main():
    while True:
        try:
            action = input("Choose operation (1 for encode, 2 for decode, 3 for end): ").strip().lower()

            if action == "1":
                encode()
            elif action == "2":
                decode()
            elif action == "3":
                break
            else:
                raise ValueError
        except ValueError:
            print("That is not a recognised action. Please try again.")


main()"""


def encode(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result


def decode(message, shift):
    return encode(message, -shift)


operation = input("Choose operation (1 for encode, 2 for decode): ")
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if operation == "1":
    result = encode(message, shift)
    print("\nEncoded message:", result)

elif operation == "2":
    result = decode(message, shift)
    print("\nDecoded message:", result)

else:
    print("\nInvalid operation. Please choose 1 or 2.")