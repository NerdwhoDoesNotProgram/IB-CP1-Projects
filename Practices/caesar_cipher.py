# IB - Caesar_Cipher.py

def encode(message, shift):
    """This function takes in the user inputed message and shift value. It avoids changing non-letter characters, and takes the ASCII of the letter, and applies the shift to it, changing it back to a letter. It then adds the new character to the empty 'result' string."""
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
    """This decodes the message by running the encode funciton, but using the negative shift valiue to shift it back."""
    return encode(message, -shift)

def main():
    """This aks the user for what operstion they want to do, and then based on what it is, it asks for the massage and shift value, and calls either decode, encode, or it ends the program. If it is neither 1, 2, or 3, then it raises a value error, which loops back to the top."""
    while True:
        try:
            operation = input("Choose operation (1 for encode, 2 for decode, 3 for end program): ").strip().lower()

            if operation == "1" or operation == "e"  or operation == "encode":
                message = input("Enter the message: ")
                shift = int(input("Enter the shift value: "))
                result = encode(message, shift)
                print("\nEncoded message:", result)

            elif operation == "2" or operation == "d"  or operation == "decode":
                message = input("Enter the message: ")
                shift = int(input("Enter the shift value: "))
                result = decode(message, shift)
                print("\nDecoded message:", result)
            
            elif operation == "3" or operation == "end"  or operation == "end program":
                print("Program ended")
                break
            
            else:
                raise ValueError

        except ValueError:
            print("That is not a recognised operation. Please try again between 1 or 2.")

main()