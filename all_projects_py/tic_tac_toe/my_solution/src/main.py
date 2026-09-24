class TicTacToe:
    """Represent a simple 3x3 Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize the game board with nine empty cells."""
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    def show_board(self):
        """Display the current state of the game board."""
        for i in self.board:
            print(i)
    
    def circle(self):
        """Allow player O to choose an empty cell and place an O."""
        # Ask player O to choose a cell from 1 to 9.
        target = int(input('player O, choose a cell: '))

        # Convert the cell number into row and column indexes.
        row = (target - 1) // 3
        col = (target - 1) % 3

        # Place O if the selected cell is empty.
        if self.board[row][col] == ' ':
            self.board[row][col] = 'O'

        # If the cell is occupied, ask the player to choose again.
        else:
            print('cell is already occupied, try again')
            self.circle()

    def cross(self):
        """Allow player X to choose an empty cell and place an X."""
        # Ask player X to choose a cell from 1 to 9.
        target = int(input('player X, choose a cell: '))

        # Convert the cell number into row and column indexes.
        row = (target - 1) // 3
        col = (target - 1) % 3

        # Place X if the selected cell is empty.
        if self.board[row][col] == ' ':
            self.board[row][col] = 'X'

        # If the cell is occupied, ask the player to choose again.
        else:
            print('cell is already occupied, try again')
            self.cross()


def start():
    """Start and run the Tic-Tac-Toe game."""
    # Create a new Tic-Tac-Toe game.
    game = TicTacToe()

    # Display the empty board before the game starts.
    game.show_board()

    # Keep the game running while win is True.
    win = True

    while win:
        # Player O makes a move.
        game.circle()
        game.show_board()

        # Player X makes a move.
        game.cross()
        game.show_board()

        # Check the first row for a win by player O.
        if game.board[0][0] == game.board[0][1] == game.board[0][2] == ('O'):
            win = False
            print('player', game.board[0][0], 'wins')
            return
        
        # Check the second row for a win by player O.
        if game.board[1][0] == game.board[1][1] == game.board[1][2] == ('O'):
            win = False
            print('player', game.board[1][0], 'wins')
            return
        
        # Check the third row for a win by player O.
        if game.board[2][0] == game.board[2][1] == game.board[2][2] == ('O'):
            win = False
            print('player', game.board[2][0], 'wins')
            return
        
        # Check the first column for a win by player O.
        if game.board[0][0] == game.board[1][0] == game.board[2][0] == ('O'):
            win = False
            print('player', game.board[0][0], 'wins')
            return
        
        # Check the main diagonal for a win by player O.
        if game.board[0][0] == game.board[1][1] == game.board[2][2] == ('O'):
            win = False
            print('player', game.board[1][1], 'wins')
            return

        # Check whether all cells are occupied.
        if all(cell != ' ' for row in game.board for cell in row):
            win = False
            print("Draw!")
            return


if __name__ == '__main__':
    start()
