import random


def monty_hall_game(switch_doors):
    """Simulate one game of the Monty Hall problem.

    Args:
        switch_doors: Whether the player switches to the remaining door.

    Returns:
        True if the player wins the car, otherwise False.
    """
    doors = ['car', 'goat', 'goat']

    # Randomly place the car and goats behind the three doors.
    random.shuffle(doors)

    # The player randomly chooses one door.
    initial_choice = random.choice(range(3))

    if switch_doors:
        # Find the goat doors that were not initially chosen.
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']

        # Monty reveals one of the available goat doors.
        door_revealed = random.choice(doors_revealed)

        # The player switches to the only remaining unopened door.
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]  # noqa: RUF015
    else:
        # The player keeps their original choice.
        final_choice = initial_choice

    # Check whether the player's final choice contains the car.
    return doors[final_choice] == 'car'


def simulate_game(num_games):
    """Simulate the Monty Hall game with and without switching.

    Args:
        num_games: Number of games to simulate for each strategy.

    Returns:
        A tuple containing the win rates without switching and with
        switching.
    """
    # Count wins when the player keeps the initial choice.
    num_wins_without_switch = sum(
        monty_hall_game(False) for _ in range(num_games)
    )

    # Count wins when the player switches doors.
    num_wins_with_switch = sum(
        monty_hall_game(True) for _ in range(num_games)
    )

    # Calculate the win rate for each strategy.
    return (
        num_wins_without_switch / num_games,
        num_wins_with_switch / num_games,
    )


if __name__ == '__main__':
    # Ask the user how many games should be simulated.
    num_games = int(input('Enter the number of games to simulate: '))

    # Run the simulation using both strategies.
    win_rate_without_switch, win_rate_with_switch = simulate_game(num_games)
