"""
Author: Ali Abbaspour
Date: 2026-09-14
Description: this is a simple Rock Paper Scissors game
"""


import random


class RockPaperScissors:
    """Main class for Rock Paper Scissors game.
    """
    def __init__(self, name: str):
        self.choices = ['rock', 'paper', 'scissors']
        self.name = name
    def get_player_choice(self):
        user_choice = input(f"{self.name}, choose your tool between {self.choices}: ")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        else:
            print('Invalid choice, please try again')
            return self.get_player_choice()
        
    def get_computer_choice(self):
        """Get computer choice randomly from choices: rock, paper, scissors."""
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide the winner based on user and computer choices.

        :param user_choice: the choice made by the user (rock, paper, or scissors)
        :param computer_choice: the choice made by the computer (rock, paper, or scissors)
        :return: a string indicating the result of the game (tie, user wins, or computer wins)
        """
        if user_choice == computer_choice:
            return "It's a tie!"
        win_combination = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combination:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return f"{self.name} wins!"
            else:
                return 'you lose'

    def play(self):
        """play the game by getting user and computer choices, printing them, and deciding the winner."""
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"{self.name} chose {user_choice} and computer chose {computer_choice}")
        print(f'computer chose {computer_choice}')
        print(self.decide_winner(user_choice, computer_choice))

if __name__ == '__main__':
    game = RockPaperScissors(input("Enter your name: "))
    
    while True:
        game.play()

        continue_game = input("Do you want to play again? (Enter any key to continue or 'no' to exit): ")
        if continue_game.lower() == "no":
            break
