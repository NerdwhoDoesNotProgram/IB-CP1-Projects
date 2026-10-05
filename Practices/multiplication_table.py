# IB - Multiplicaiton Table

"""def main():
    def table(spacing, size):  
        print("Multiplication Table")
        print("     ", end="")

        for i in range(1, size + 1):
            print(f"{i:{spacing}}", end="")
        print("\n" + "_" * ((size*spacing)+5))
       
        for c in range(1, size + 1):
            
            print(f"{c:2} |", end="")
            
           
            for r in range(1, size + 1):
                product = c * r
                print(f"{product:{spacing}}", end="")
            
            
            print()

    size = int(input("Enter the size of the multiplication table: "))

    if size <= 3:
        spacing = 2
        table(spacing, size)
        return spacing, size
    elif size <= 9:
        spacing = 3
        table(spacing, size)
        return spacing, size

    elif size <= 31:
        spacing = 4
        table(spacing, size)
        return spacing, size
    elif size <= 99:
        spacing = 5
        table(spacing, size)
        return spacing, size
    elif size <= 316:
        spacing = 6
        table(spacing, size)
        return spacing, size
    elif size <= 999:
        spacing = 7
        table(spacing, size)
        return spacing, size
    elif size <= 3162:
        spacing = 8
        table(spacing, size)
        return spacing, size
    elif size <= 9999:
        spacing = 9
        table(spacing, size)
        return spacing, size
    elif size <= 31622:
        spacing = 10
        table(spacing, size)
        return spacing,size
    else:
        spacing = 4
        #size = 12
        table(spacing, size=12)
        return spacing, size

main()"""

def table(spacing, size):  
        print("Multiplication Table")
        print("     ", end="")

        for i in range(1, size + 1):
            print(f"{i:{spacing}}", end="")
        print("\n" + "_" * ((size*spacing)+5))
       
        for c in range(1, size + 1):
            
            print(f"{c:2} |", end="")
            
           
            for r in range(1, size + 1):
                product = c * r
                print(f"{product:{spacing}}", end="")
            
            
            print()

def main():
    while True:
        try:
                size = input("Enter the size of the multiplication table: ").strip()

                if not size.isnumeric():
                    raise ValueError
                else:
                    size = int(size)
                    if size <= 3:
                        spacing = 2
                        table(spacing, size)
                        return spacing, size
                    elif size <= 9:
                        spacing = 3
                        table(spacing, size)
                        return spacing, size
                    elif size <= 31:
                        spacing = 4
                        table(spacing, size)
                        return spacing, size
                    elif size <= 99:
                        spacing = 5
                        table(spacing, size)
                        return spacing, size
                    elif size <= 316:
                        spacing = 6
                        table(spacing, size)
                        return spacing, size
                    elif size <= 999:
                        spacing = 7
                        table(spacing, size)
                        return spacing, size
                    elif size <= 3162:
                        spacing = 8
                        table(spacing, size)
                        return spacing, size
                    elif size <= 9999:
                        spacing = 9
                        table(spacing, size)
                        return spacing, size
                    elif size <= 31622:
                        spacing = 10
                        table(spacing, size)
                        return spacing,size
                    else:
                        spacing = 4
                        #size = 12
                        table(spacing, size=12)
                        return spacing, size
        
        except ValueError:
            print("That is not a valid integer. Please try again.")



main()