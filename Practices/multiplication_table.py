# IB - Multiplicaiton Table

def main():
    def table(spacing, size):  
        print("Multiplication Table")
        print("     ", end="")
        for i in range(1, size + 1):
            print(f"{i:{spacing}}", end="")
        print("\n" + "_" * 55)
        # Generate the multiplication table grid
        for c in range(1, size + 1):
            # Print the row label
            print(f"{c:2} |", end="")
            
            # Print the products for that row
            for r in range(1, size + 1):
                product = c * r
                print(f"{product:{spacing}}", end="")
            
            # Move to the next line after completing a row
            print()

    size = int(input("Enter the size of the multiplication table: "))

    if size <= 3:
        spacing = 2
        table(spacing, )
        return spacing
    elif size <= 9:
        spacing = 3
        table(spacing, )
        return spacing

    elif size <= 31:
        spacing = 4
        table(spacing, )
        return spacing
    elif size <= 99:
        spacing = 5
        table(spacing, )
        return spacing
    elif size <= 316:
        spacing = 6
        table(spacing, )
        return spacing
    elif size <= 999:
        spacing = 7
        table(spacing, )
        return spacing
    elif size <= 3162:
        spacing = 8
        table(spacing, )
        return spacing
    elif size <= 9999:
        spacing = 9
        table(spacing, )
        return spacing
    elif size <= 31622:
        spacing = 10
        table(spacing, )
        return spacing
    else:
        spacing = 4
        #size = 12
        table(spacing, size=12)
        return spacing, size

main()