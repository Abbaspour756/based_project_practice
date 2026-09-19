import random


def put_randomly():
    """Randomly assign two goats and one car to three doors.

    Returns:
        dict: A dictionary containing three doors and their randomly
        assigned values.
    """
    doors = {
        1: None,
        2: None,
        3: None
    }

    values = ["goat", "car", "goat"]

    # Randomly shuffle the values before assigning them to the doors.
    random.shuffle(values)

    # Assign each shuffled value to its corresponding door.
    for door, value in zip(doors, values):
        doors[door] = value

    return doors


def choose_door():
    """Let the player choose a door and reveal a goat behind another door.

    Returns:
        tuple: The revealed goat door, the original door configuration,
        and the player's initial choice.
    """
    doors = put_randomly()

    # Keep a copy of the original configuration so it is not modified
    # when a goat is removed from the temporary dictionary.
    doors2 = doors.copy()

    choice = int(input("Choose your door between 1, 2, 3: "))

    # Validate the player's choice.
    if choice >= 1 and choice <= 3:
        pass
    else:
        print("Invalid choice")
        print("Please choose a door only between 1, 2, 3")
        choose_door()

    # Remove the door selected by the player from the temporary dictionary.
    if choice == 1:
        del doors[1]

    if choice == 2:
        del doors[2]

    if choice == 3:
        del doors[3]

    value = "goat"

    # Find a remaining door containing a goat and reveal it.
    for key, val in doors.items():
        if val == value:
            print(f"This door ({key}) has a goat")
            break

    return key, doors2, choice


def change_door():
    """Run one round of the Monty Hall game.

    The player chooses a door, the host reveals a goat, and the player
    decides whether to change their original choice.
    """
    key, doors2, choice = choose_door()

    # Remove the revealed goat door from the original configuration.
    del doors2[key]

    decide = input("Do you want to change your choice? y/n: ")

    if decide == "y":
        # Select the only remaining door that was not originally chosen.
        for key, value in doors2.items():
            if key != choice:
                print(f"You choose the door {key} and it was a {value}")
    else:
        # Keep the original choice.
        print(f"You choose the door {choice} and it was a {doors2[choice]}")


if __name__ == "__main__":
    change_door()
