# IB - Escape room

def escape_room():
    room_description = (
        "You blink open your eyes to the harsh, flickering glow of CRT monitors inside a windowless computer lab. "
        "A faded brass plaque next to the heavy metal door reads: 'Designated Facility: ROOM 101'. "
        "The heavy metal door is locked tight, and a glowing biometric keypad waits next to it.\n\n"
        "The room is an absolute mess of distractions:\n"
        "- A sticky mechanical keyboard on the nearest desk has a Post-it note reading: 'TODO: Fix the infinite loop before lunch!' "
        "and another note scribbled with a chaotic Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13...`.\n"
        "- Stacks of ancient Python documentation manuals are piled high, open to a chapter on `SyntaxError` exceptions.\n"
        "- On the back wall, someone has taped a massive, incredibly detailed 12-bullet-point poster for the "
        "'Future Accountants of America' complete with a pie chart showing last year's chocolate-chip versus oatmeal-raisin "
        "cookie sales ratio (64% to 36%) and a laminated photo of their club advisor proudly holding an ordinary stapler.\n"
        "- Above the whiteboard, a plaque reads: 'Welcome to the place where all programs begin their execution.'\n\n"
        "You squint at the keypad. What is this place called again?"
    )

    correct_code = "101"
    max_attempts = 3
    tries = 0

    print("=== WELCOME TO THE CODING LAB ESCAPE ROOM ===")
    print(room_description)

    while tries < max_attempts:
        guess = input("\nEnter the keypad code: ").strip()

        if guess == correct_code or guess.upper() == "ROOM 101":
            print("\n*CLICK!* The biometric scanner flashes green. The door swings open. You Escaped! ")
            break
        else:
            tries += 1
            remaining = max_attempts - tries
            print(f"Incorrect code! Tries remaining: {remaining}")
            
            if tries == 1:
                print("Hint: Ignore the accountants and the math sequences. Think about what room you are trapped in—what kind of lab is this?")
            elif tries == 2:
                print("Hint: It's a 'Code... (ing room)' combined with a standard room number.")

    if tries == max_attempts:
        print("\nYou ran out of attempts! The keypad flashes red and locks permanently. You are trapped forever! ")

escape_room()