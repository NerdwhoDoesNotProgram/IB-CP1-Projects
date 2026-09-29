# Where I write out some code that might work.

def show_list(shopping_list):
    print("\n--- Current Shopping List ---")
    if not shopping_list:
        print("Your list is currently empty.")
    else:
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    print("-----------------------------\n")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip().capitalize()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    if not shopping_list:
        print("List is empty. Nothing to remove.")
        return
    
    item = input("Enter the item to remove: ").strip().capitalize()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print(f"'{item}' was not found in the list.")

def mark_done(shopping_list):
    if not shopping_list:
        print("List is empty. Nothing to mark as done.")
        return
    
    item = input("Enter the item to mark as done: ").strip().capitalize()
    if item in shopping_list:
        index = shopping_list.index(item)

        if not shopping_list[index].endswith("(DONE)"):
            shopping_list[index] = f"{shopping_list[index]} (DONE)"
            print(f"'{item}' marked as done!")
        else:
            print("That item is already marked as done.")
    else:
        print(f"'{item}' was not found in the list.")

shopping_list = []

while True:
    action = input("Choose an action (add, remove, view, done, exit): ").lower().strip()
    
    if action == "add":
        add_item(shopping_list)
        show_list(shopping_list)
    elif action == "remove":
        remove_item(shopping_list)
        show_list(shopping_list)
    elif action == "view":
        show_list(shopping_list)
    elif action == "done":
        mark_done(shopping_list)
        show_list(shopping_list)
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please choose: add, remove, view, done, or exit.")