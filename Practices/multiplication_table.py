# IB - Multiplicaiton Table

def table(spacing):  
    print("Multiplication Table")
    print("     ", end="")
    for i in range(1, size + 1):
        print(f"{i:spacing}", end="")
    print("\n" + "_" * 55)
    # Generate the multiplication table grid
    for c in range(1, size + 1):
        # Print the row label
        print(f"{c:2} |", end="")
        
        # Print the products for that row
        for r in range(1, size + 1):
            product = c * r
            print(f"{product:spacing}", end="")
        
        # Move to the next line after completing a row
        print()

def main():
    size = int(input("Enter the size of the multiplication table: "))

    if size <= 31:
        spacing = 4
        table(spacing)
        return spacing
    elif size <= 99:
        spacing = 5
        table(spacing)
        return spacing

main()