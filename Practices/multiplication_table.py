# IB - Multiplicaiton Table

size = int(input("Enter the size of the multiplication table: "))

if size < 12:

elif size <= 20:
    print("Multiplication Table")

    print("     ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print("\n" + "_" * 55)

    # Generate the multiplication table grid
    for c in range(1, size + 1):
        # Print the row label
        print(f"{c:2} |", end="")
        
        # Print the products for that row
        for r in range(1, size + 1):
            product = c * r
            print(f"{product:4}", end="")
        
        # Move to the next line after completing a row
        print()
