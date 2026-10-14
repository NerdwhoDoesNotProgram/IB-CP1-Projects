# IB - Escape room

import time, sys


def escape_room():
    room_description1 = (
        "You blink open your eyes to the harsh, flickering glow of CRT monitors inside a windowless computer lab. "
        "A timer on hte wall counts down." )
        
    room_description2 = (
        "A faded brass plaque next to the heavy metal door reads: 'Designated Facility: ROOM 101'. "
        "The heavy metal door is locked tight, and a glowing biometric keypad waits next to it.\n\n"
        "You squint at the keypad. What could the code be?"
        )

    correct_code = "101"
    max_attempts = 4
    tries = 0
    duration = 10 #240
    start_time = time.perf_counter()

    print("=== WELCOME TO THE CODING LAB ESCAPE ROOM ===")
    print(room_description1)
    time.sleep(1)
    print("04:00")
    time.sleep(1)
    print("03:59")
    time.sleep(1)
    print("03:58...")
    time.sleep(1)
    print(room_description2)

    

    while tries < max_attempts:

        action = input("\n What action do you want to do? (1: look, 2: timer, 3: enter code)").strip().lower()

        if action == "1" or action == "look" or action == "l":
            look()
        elif action == "2" or action == "timer" or action == "t":
            timer(time_elapsed)
            return time_elapsed
        elif action == "3" or action == "enter code" or action == "enter" or action == "code" or action == "e" or action == "c":
            guess = input("\nEnter the keypad code: ").strip()

            time_elapsed = time.perf_counter() - start_time

            if time_elapsed >= duration:
                print("\nThe timer counts down...")
                time.sleep(1)
                print("00:04")
                time.sleep(1)
                print("00:03")
                time.sleep(1)
                print("00:02")
                time.sleep(1)
                print("00:01")
                time.sleep(1)
                print("00:00")
                print("As the timer hits zero, the keypad flashes red and locks permanently. "
                    "You took too long and are trapped forever!")
                sys.exit()

            if guess == correct_code or guess.upper() == "ROOM 101":
                print("\n*CLICK!* The biometric scanner flashes green. The door swings open. You Escaped!")
                sys.exit()

            else:
                tries += 1
                remaining = max_attempts - tries
                print(f"Incorrect code! Tries remaining: {remaining}")
                    
                if tries == 1:
                    print("Hint: Ignore the accountants and the math sequences. Think about what room you are trapped in—what kind of lab is this?")

                elif tries == 2:
                    print("Hint: It's a 'Code... (ing room)' combined with a standard room number.")
                
                elif tries == 3:
                    print("Hint: What is the room number?")

    print("\nYou ran out of attempts! The keypad flashes red and locks permanently. You are trapped forever!")
    sys.exit()

def look():
    room_description_look = (
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

def timer(time_elapsed):

    print("You glance up at the wall to the timer. it is still counting down...")

    for i in range(4):
        mins, secs = divmod(time_elapsed, 60)

        formatted_time = f"{int(mins):02d}:{secs:02d}"

        time.sleep(1)
        print(f"{formatted_time}")
    print("...")

escape_room()