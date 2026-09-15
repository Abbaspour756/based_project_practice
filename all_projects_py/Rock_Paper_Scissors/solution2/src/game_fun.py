import random


def get_player_choice():
    """Get player choice.
    """
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    if player_choice.lower() not in choices:
        print("Invalid choice. Please try again.")
        return get_player_choice()
    return player_choice


def get_computer_choice():
    """Get computer choice.
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice


def decide_winner(user_choice: str, computer_choice: str) -> str:
    """Decide the winner of the game.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
def play():
    """Play the game.
    """
    user_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(decide_winner(user_choice, computer_choice))
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play()
