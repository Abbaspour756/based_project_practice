"""A simple command-line Tic-Tac-Toe game."""

import random


class TicTacToe:
    """Manage the board and turns for a two-player Tic-Tac-Toe game."""

    def __init__(self, ):
        """Initialize an empty board and set X to play first."""
        self.board = [' '] * 10
        self.player_turn = 'X'

    def get_random_first_player(self):
        """Return a randomly selected starting player."""
        return random.choice(['X', 'O'])

    def show_board(self):
        """Print the current board."""
        print('\n')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-----')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-----')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')
    
    def swap_player_turn(self):
        """Switch the active player and return the new player."""
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn
    
    def is_board_filled(self):
        """Return whether all playable cells are occupied."""
        return ' ' not in self.board[1:]
    
    def fix_spot(self, cell, player):
        """Place the specified player's mark in the given cell."""
        self.board[cell] = player
    
    def has_player_won(self, player):
        """Return whether the specified player has a winning line."""
        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
            (1, 5, 9), (3, 5, 7)              # diagonals
        ]

        # Check whether the player's mark fills any winning combination.
        for combination in win_combinations:
            if all(self.board[cell] == player for cell in combination):
                return True
            
        return False

    def start(self):
        """Run the game loop, prompting players until the game ends."""
        while True:
            self.show_board()
            print(f'player {self.player_turn} turn')
            cell = int(input('enter cell number from 1 to 9:'))

            # Place a mark only if the selected cell is empty and valid.
            if self.board[cell] == ' ' and cell in range(1, 10):
                self.fix_spot(cell, self.player_turn)

                # Check for a win before checking for a draw.
                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f'player {self.player_turn} won')
                    break

                if self.is_board_filled():
                    self.show_board()
                    print('draw')
                    break
                
                self.swap_player_turn()

            else:
                print()

# Create and start a game when this file is run directly.
if __name__ == '__main__':
    game = TicTacToe()
    game.start()
    