import random


def play_game() -> str:
    '''
    In this function the game will be played
    It is about choosing a tool between "Rock", "Paper", "Scissors"
    You are going to play against the computer
    

    args:
        tool: The tool you choose in the RockPaperScissors class
    
    return:
        The result of the game
    '''
    # in this section the player will choose his tool between "Rock", "Paper", "Scissors"
    class RockPaperScissors:
        def __init__(self, tool):
            if tool.lower() not in ['rock', 'paper', 'scissors']:
                raise ValueError('Invalid tool \nIt should be "Rock", "Paper", "Scissors"')
            self.tool = tool.lower()

    our_tool = RockPaperScissors(input('Enter a tool that you want to use between "Rock", "Paper", "Scissors": '))

    main_tool = our_tool.tool


    # in this section the robot will choose his tool randomly
    tools = ["rock", "paper", "scissors"]


    robot_tool = random.choice(tools)

    # this the all possible outcomes of the game
    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    # in this section the game will be played
    if main_tool == robot_tool:
        print("Draw!")
    elif wins_against[main_tool] == robot_tool:
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    print(f"Robot chose: {robot_tool}\n")
    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")


if __name__ == '__main__':
    play_game()