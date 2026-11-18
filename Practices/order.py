
# IB - Period ___ - Order Up

# The Cheesecake Factory - Orem, Utah
# Menu reference:
# https://www.thecheesecakefactory.com/location/orem-ut/menu
# https://www.thecheesecakefactory.com/veg

# PSEUDOCODE:
# 1. Create a dictionary containing menu categories, items, and prices.
# 2. Display the menu if the customer wants to see it.
# 3. Ask the customer to select a drink.
# 4. Ask the customer to select a main course or kids meal.
# 5. Ask the customer to select two side dishes.
# 6. Allow the customer to add an appetizer and dessert.
# 7. Validate all selections.
# 8. Calculate the total cost.
# 9. Display the customer's complete order and total.


# MENU

menu = {

    "Drinks": {
        "Water": 0.00,
        "Coke": 3.75,
        "Arnold Palmer": 4.50,
        "Paradise Punch": 6.00,
        "Coconut Limeade": 6.00,
        "Pineapple Cherry Limeade": 6.00,
        "Pineapple Coconut Dream": 6.00,
        "Sparkling Yuzu Lemonade": 6.00,
        "Passion Mint Fizz": 6.00,
        "Cold Brew Coffee": 5.50,
        "Fiji Water": 4.95,
        "Fresh Orange Juice": 7.50,
        "Apple Juice": 6.50
    },

    "Appetizers": {
        "Roadside Sliders": 15.95,
        "Chicken Pot Stickers": 16.95,
        "Tex Mex Eggrolls": 13.95,
        "Quesadilla": 13.95,
        "Thai Chili Shrimp": 15.95,
        "Avocado Eggrolls": 16.95,
        "Fried Macaroni and Cheese": 15.95,
        "Fried Calamari": 17.95,
        "Eggroll Sampler": 16.95,
        "Spicy Tuna": 18.95,
        "Ahi Poke Nachos": 18.95,
        "Hot Spinach and Cheese Dip": 17.50,
        "Buffalo Blasts": 17.95,
        "Thai Lettuce Wraps with Chicken": 19.95
    },

    "Vegitarian Appetizers": {
        "Quesadilla": 13.95,
        "Avacado Eggrolls": 16.95,
        "Hot Spinach and Cheese Dip": 17.50,
        "Thai Lettice Wraps with Avacado": 19.95,
        "Small Thai Lettuce Wraps with Avacado": 13.95,
        "Pretzel Bites With Cheddar Cheese Fondue": 15.95
    },

    "Main Course": {

        # Bowls and Flatbread Pizzas
        "Chicken Katsu Bowl": 19.95,
        "Mediterranean Bowl": 18.95,
        "Baja Bowl with Grilled Chicken": 19.95,
        "Cheese Flatbread Pizza": 17.95,
        "Margherita Flatbread Pizza": 17.95,
        "Pepperoni Flatbread Pizza": 17.95,
        "Bee Sting Flatbread Pizza": 17.95,

        # Burgers
        "Old Fashioned Burger": 17.95,
        "Double Smash Cheeseburger": 19.95,
        "Bistro Burger": 19.95,
        "Americana Cheeseburger": 18.95,
        "Smokehouse BBQ Burger": 19.95,
        "Veggie Burger": 18.95,

        # Sandwiches
        "Chicken Shawarma": 18.50,
        "Chicken Salad Sandwich": 18.50,
        "Cuban Sandwich": 19.50,
        "The Club": 19.95,
        "Grilled Chicken and Avocado Club": 19.95,
        "Crispy Factory Fish Sandwich": 19.95,
        "Modern Cheesesteak": 26.95,

        # Salads
        "Cobb Salad": 19.95,
        "Tossed Green Salad": 12.50,
        "Caesar Salad": 14.95,
        "Tai Chicken Salad": 19.50,
        "Barbeque Ranch Chicken Salad": 19.95,
        "Chinese Chicken Salad": 19.95,
        "Santa Fe Salad": 19.95,
        "Vegan Cobb Salad": 18.95,
        "Sheila's Chicken and Avocado Salad": 19.95,

        # Pastas and Specialties
        "Fettuccini Alfredo": 17.95,
        "Four Cheese Pasta": 17.95,
        "Pasta Carbonara": 17.95,
        "Pasta Da Vinci": 17.95,
        "Spicy Rigatoni Vodka": 17.95,
        "Spaghetti and Meatballs": 17.95,
        "Louisiana Chicken Pasta": 17.95,
        "Chicken Piccata": 17.95,
        "Famous Factory Meatloaf": 17.95,

        # Fish and Seafood
        "Fish and Chips": 24.50,
        "Shrimp Scampi": 28.95,
        "Jamaican Black Pepper Shrimp": 25.95,
        "Grilled Salmon": 27.95,
        "Cajun Salmon": 29.95,
        "Miso Salmon": 29.95,
        "Grilled Branzino": 28.95,

        # Steaks
        "Carne Asada Steak": 26.95,
        "Steak Frites": 29.95,
        "Steak Diane": 29.95,
        "Grilled Rib-Eye Steak": 43.95,
        "Filet Mignon": 49.95
    },

    "Vegitarian Main Course": {
        # Flatbread Pizzas
        "Cheese Flatbread Pizza": 12.95,
        "Margherita Flatbread Pizza": 13.50,
        "Fresh Basil, Tomato and Cheese Flatbread Pizza": 13.95,
        # Burgers
        "Veggie Burger": 18.95,
        # Salads
        "Tossed Green Salad": 12.50,
        "Vegan Cobb Salad": 18.95,
        # Pastas
        "Fettuccini Alfredo": 22.95,
        "Four Cheese Pasta": 23.95,
        "Evelyn's Favorite Pasta": 23.50
    },

    "Side Dishes": {
        "French Fries": 6.95,
        "Sweet Potato Fries": 7.95,
        "Green Beans": 7.95,
        "Fresh Corn": 7.95,
        "Mashed Potatoes": 7.95,
        "Sauteed Spinach": 7.95,
        "Macaroni & Cheese": 9.95,
        "Broccoli": 7.95,
        "Grilled Asparagus": 9.50,
        "Steamed White Rice": 2.50,
        "Steamed Brown Rice": 2.95
    },

    "Desserts & Milkshakes": {

        # Cheesecakes
        "Original Cheesecake": 10.95,
        "Fresh Strawberry Cheesecake": 10.95,
        "Oreo Dream Extreme Cheesecake": 10.95,
        "Ultimate Red Velvet Cheesecake": 10.95,
        "White Chocolate Raspberry Truffle": 10.95,
        "Chocolate Mousse Cheesecake": 10.95,
        "Fresh Banana Cream Cheesecake": 10.95,
        "Salted Caramel Cheesecake": 10.95,
        "Key Lime Cheesecake": 10.95,

        # Other Desserts
        "Linda's Fudge Cake": 10.95,
        "Carrot Cake": 10.95,
        "Tiramisu": 10.95,
        "Warm Apple Crisp": 10.95,
        "Fresh Strawberry Shortcake": 10.95,
        "Hot Fudge Sundae": 12.95,
        "Godiva Chocolate Brownie Sundae": 14.50,

        # Milkshakes
        "Vanilla Milkshake": 9.95,
        "Chocolate Milkshake": 9.95,
        "Strawberry Milkshake": 9.95,
        "Oreo Milkshake": 10.95,

        # Smoothies
        "Tropical Smoothie": 8.95,
        "Peach Smoothie": 8.95,
        "Strawberry Fruit Smoothie": 8.95,
        "Frozen Iced Mango": 9.50
    },

    "Kids Menu": {
        "Kids Roadside Sliders": 9.50,
        "Kids Pigs in a Blanket": 10.95,
        "Kids Pasta with Butter and Parmesan": 8.95,
        "Kids Pasta with Marinara Sauce": 10.50,
        "Kids Pasta with Alfredo Sauce": 10.95,
        "Kids Spaghetti with Meatball": 11.95,
        "Kids Macaroni and Cheese": 9.50,
        "Kids Fried Chicken Strips": 9.95,
        "Kids Cheese Flatbread Pizza": 10.95,
        "Kids Pepperoni Flatbread Pizza": 11.95,
        "Kids Quesadilla": 9.95,
        "Kids Chicken Quesadilla": 11.95,
        "Kids Grilled Cheese Sandwich": 9.50,
        "Kids Grilled Chicken": 11.50,
        "Kids Grilled Salmon": 15.50
    }
}

# RECORDS THE ORDER
order = {
    "Drink": "",
    "Main Course": "",
    "Main Category": "",
    "Side Dishes": [],
    "Appetizers": [],
    "Desserts": []
}

# DISPLAY MENU
 
def show_menu():

    print("\n========== THE CHEESECAKE FACTORY ==========")

    for category, items in menu.items():

        print(f"\n--- {category} ---")

        for name, price in items.items():

            print(f"{name}: ${price:.2f}")

# GET A MENU ITEM
def get_item(category):

    items = menu[category]

    while True:

        print(f"\n--- {category} ---")

        for number, (name, price) in enumerate(items.items(), 1):

            print(f"{number}. {name} - ${price:.2f}")

        choice = input("\nEnter the item number or name: ").strip()

        # Check if the user entered a number
        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(items):

                return list(items.keys())[choice - 1]

        # Check if the user entered an item name
        for name in items:

            if choice.lower() == name.lower():

                return name

        print("\nInvalid selection. Please try again.")

# GET DRINK
def get_drink():

    return get_item("Drinks")

# GET MAIN COURSE
def get_main():

    while True:

        print("\nWould you like a regular meal or a kids meal?")
        print("1. Regular Main Course")
        print("2. Kids Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            order["Main Category"] = "Main Course"
            return get_item("Main Course")

        elif choice == "2":

            order["Main Category"] = "Kids Menu"
            return get_item("Kids Menu")

        else:

            print("Invalid selection. Please enter 1 or 2.")
 
# GET SIDE DISHES
def get_sides():

    sides = []

    for number in range(2):

        print(f"\nChoose side dish {number + 1}:")

        side = get_item("Side Dishes")

        sides.append(side)

    return sides
 
# OPTIONAL MENU ITEMS
def add_optional_items(category, order_category):

    while True:

        choice = input(
            f"\nWould you like to add {category.lower()}? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:

            item = get_item(category)

            order[order_category].append(item)

            print(f"{item} added to your order!")

            # Ask if they want another
            another = input(
                "Would you like to add another? (yes/no): "
            ).strip().lower()

            if another not in ["yes", "y"]:

                break

        elif choice in ["no", "n"]:

            break

        else:

            print("Please enter yes or no.")

# CALCULATE COST
def cost():

    total = 0

    # Drink
    total += menu["Drinks"][order["Drink"]]

    # Main course
    main_category = order["Main Category"]

    total += menu[main_category][order["Main Course"]]

    # Side dishes
    for side in order["Side Dishes"]:

        total += menu["Side Dishes"][side]

    # Appetizers
    for appetizer in order["Appetizers"]:

        total += menu["Appetizers"][appetizer]

    # Desserts
    for dessert in order["Desserts"]:

        total += menu["Desserts & Milkshakes"][dessert]

    return total

# REPEAT ORDER
def repeat_order():

    print("\n========== YOUR ORDER ==========")

    print(f"\nDrink: {order['Drink']}")

    print(f"Main Course: {order['Main Course']}")

    print("\nSide Dishes:")

    for side in order["Side Dishes"]:

        print(f"- {side}")

    if order["Appetizers"]:

        print("\nAppetizers:")

        for appetizer in order["Appetizers"]:

            print(f"- {appetizer}")

    if order["Desserts"]:

        print("\nDesserts & Milkshakes:")

        for dessert in order["Desserts"]:

            print(f"- {dessert}")

    print("\n--------------------------------")

    print(f"Total Cost: ${cost():.2f}")

    print("================================")

# MAIN PROGRAM
def main():

    print("\nWelcome to The Cheesecake Factory!")
    print("We are happy to serve you!")

    # Ask whether the customer wants to see the menu
    while True:

        choice = input(
            "\nWould you like to view the full menu? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:

            show_menu()
            break

        elif choice in ["no", "n"]:

            break

        else:

            print("Please enter yes or no.")

    # Collect the required order items
    print("\nLet's start your order!")

    order["Drink"] = get_drink()

    order["Main Course"] = get_main()

    order["Side Dishes"] = get_sides()

    # Offer optional items
    add_optional_items("Appetizers", "Appetizers")

    add_optional_items("Desserts & Milkshakes", "Desserts")

    # Display the completed order
    repeat_order()

    print("\nThank you for visiting The Cheesecake Factory!")


main()