
# IB - Escape Room

import time


def escape_room():
    room_description1 = (
        "You blink open your eyes to the harsh, flickering glow of CRT "
        "monitors inside a windowless computer lab. "
        "A timer on the wall counts down."
    )

    room_description2 = (
        "\nA faded brass plaque next to the heavy metal door reads: "
        "'Designated Facility: ROOM 101'. "
        "The door is locked tight, and a glowing biometric keypad "
        "waits next to it.\n\n"
        "You squint at the keypad. What could the code be?"
    )

    correct_code = "101"
    max_attempts = 5
    tries = 0
    duration = 240  # 4 minutes, in seconds
    start_time = time.perf_counter()

    print("=== WELCOME TO THE CODING LAB ESCAPE ROOM ===")
    print(room_description1)
    print("04:00")
    time.sleep(1)
    print("03:59")
    time.sleep(1)
    print("03:58")
    time.sleep(1)
    print("...")
    print(room_description2)

    while tries < max_attempts:
        time_elapsed = time.perf_counter() - start_time
        time_remaining = duration - time_elapsed

        if time_remaining <= 0:
            print("\n00:00")
            print(
                "As the timer hits zero, the keypad flashes red "
                "and locks permanently. You took too long and "
                "are trapped forever!"
            )
            return

        action = input(
            "\nWhat action do you want to do? "
            "(1: look, 2: timer, 3: enter code): "
        ).strip().lower()

        time_elapsed = time.perf_counter() - start_time

        if time_elapsed >= duration:
            print("\n00:00")
            print(
                "The timer reaches zero! The keypad flashes red "
                "and locks permanently. You are trapped forever!"
            )
            return

        if action in ("1", "look", "l"):
            look()

        elif action in ("2", "timer", "t"):
            timer(duration - time_elapsed)

        elif action in (
            "3", "enter code", "enter", "code", "e", "c"
        ):
            guess = input("\nEnter the keypad code: ").strip()

            time_elapsed = time.perf_counter() - start_time

            if time_elapsed >= duration:
                print("\n00:00")
                print(
                    "The timer reaches zero! The keypad flashes red "
                    "and locks permanently. You are trapped forever!"
                )
                return

            if guess == correct_code or guess.upper() == "ROOM 101":
                print(
                    "\n*CLICK!* The biometric scanner flashes green. "
                    "The door swings open. You escaped!"
                )
                return

            tries += 1
            remaining = max_attempts - tries

            print(f"\nIncorrect code! Tries remaining: {remaining}")

            if tries == 1:
                print(
                    "Hint: Ignore the accountants and the math "
                    "sequences. Think about what room you are "
                    "trapped in—what kind of lab is this?"
                )
            elif tries == 2:
                print(
                    "Hint: It's a 'Code... (ing room)' combined "
                    "with a standard room number."
                )
            elif tries == 3:
                print("Hint: What is the room number?")

        else:
            print(
                "Invalid action. Choose 1, 2, or 3, "
                "or type look, timer, or enter code."
            )

    print(
        "\nYou ran out of attempts! The keypad flashes red "
        "and locks permanently. You are trapped forever!"
    )


def look():
    room_description_look = (
        "The room is an absolute mess of distractions:\n"
        "- A sticky mechanical keyboard on the nearest desk has a "
        "Post-it note reading: 'TODO: Fix the infinite loop before "
        "lunch!' and another note scribbled with a chaotic "
        "Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13...`.\n"
        "- Stacks of ancient Python documentation manuals are piled "
        "high, open to a chapter on `SyntaxError` exceptions.\n"
        "- On the back wall, someone has taped a massive, incredibly "
        "detailed 12-bullet-point poster for the 'Future Accountants "
        "of America', complete with a pie chart showing last year's "
        "chocolate-chip versus oatmeal-raisin cookie sales ratio "
        "(64% to 36%) and a laminated photo of their club advisor "
        "proudly holding an ordinary stapler.\n"
        "- Above the whiteboard, a plaque reads: 'Welcome to the "
        "place where all programs begin their execution.'\n\n"
        "You squint at the keypad. What is this place called again?"
    )

    print("\n" + room_description_look)


def timer(time_remaining):
    mins, secs = divmod(max(0, int(time_remaining)), 60)

    print(
        f"\nYou glance up at the wall timer. "
        f"Time remaining: {mins:02d}:{secs:02d}"
    )


escape_room()
