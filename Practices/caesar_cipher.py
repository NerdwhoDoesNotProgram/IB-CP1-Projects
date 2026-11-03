# IB - Caesar_Cipher.py

def encode():
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


main()