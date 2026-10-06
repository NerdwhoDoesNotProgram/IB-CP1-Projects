# IB - Multiplicaiton Table

def table(size):
    spacing = len(str(size * size)) + 1

    print("Multiplication Table")
    print(" " * (len(str(size)) + 2), end="")

    for i in range(1, size + 1):
        print(f"{i:{spacing}}", end="")
    print()

    print("-" * (len(str(size)) + 2 + size * spacing))

    for c in range(1, size + 1):
        print(f"{c:>{len(str(size))}} |", end="")

        for r in range(1, size + 1):
            print(f"{c * r:{spacing}}", end="")

        print()


def main():
    size = int(input("Enter the size of the multiplication table: "))
    table(size)


main()