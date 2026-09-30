# IB - Shopping List Manager

# To cross out an item, use \033[9m Item \033[0m

def show_list(shopping_list, completed_list):

    list_num = 0

    print("\n--- Current Shopping List ---")
    if not shopping_list:
        print("Your list is currently empty.")
    else: 
        for item in shopping_list:
            list_num += 1

            if item in completed_list:
                print(f"{list_num}. \033[9m{item}\033[0m")
            else:
                print(f"{list_num}. {item}")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip().capitalize()

    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list, completed_list):
    if not shopping_list:
        print("List is empty. Nothing to remove.")
        return

    item = input("Enter the item to remove: ").strip().capitalize()

    if item in shopping_list:
        shopping_list.remove(item)

        if item in completed_list:
            completed_list.remove(item)

        print(f"'{item}' has been removed.")
    else:
        print(f"'{item}' was not found in the list.")

"""def strikethrough(item):
        return "".join(char + "\u0336" for char in item)"""

def mark_done(shopping_list, completed_list):  # Need to fix how it strikes though
    
    if not shopping_list:
        print("List is empty. Nothing to mark as done.")
        return

    item = input("Enter the item to mark as done: ").strip().capitalize()

    if item in shopping_list:

        if item not in completed_list:
            completed_list.append(item)
            print(f"'{item}' has been marked as done.")
        else:
            print(f"'{item}' is already marked as done.")

    else:
        print(f"'{item}' was not found in the list.")


shopping_list = []
completed_list = []

def main():
    while True:
        action = input(
            "Choose an action (add, remove, view, done, exit): "
        ).lower().strip()

        if action == "add" or action == "a" or action == "1":
            add_item(shopping_list)
            show_list(shopping_list, completed_list)

        elif action == "remove" or action == "r" or action == "2":
            remove_item(shopping_list, completed_list)
            show_list(shopping_list, completed_list)

        elif action == "view" or action == "v" or action == "3":
            show_list(shopping_list, completed_list)

        elif action == "done" or action == "d" or action == "4":
            mark_done(shopping_list, completed_list)
            show_list(shopping_list, completed_list)

        elif action == "exit" or action == "e" or action == "5":
            print("\nGoodbye!")
            break

        else:
            print(
                "\nInvalid option, please choose: "
                "add, remove, view, done, or exit."
                )
            
main()