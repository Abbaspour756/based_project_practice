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

    win = True
    
    winning_positions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    while win:

        # Player O
        game.circle()
        game.show_board()

        for positions in winning_positions:
            player = game.board[positions[0][0]][positions[0][1]]

            if player != ' ' and all(
                game.board[row][col] == player
                for row, col in positions
            ):
                print('player', player, 'wins')
                return

        if all(cell != ' ' for row in game.board for cell in row):
            print('Draw!')
            return

        # Player X
        game.cross()
        game.show_board()

        for positions in winning_positions:
            player = game.board[positions[0][0]][positions[0][1]]

            if player != ' ' and all(
                game.board[row][col] == player
                for row, col in positions
            ):
                print('player', player, 'wins')
                return

        if all(cell != ' ' for row in game.board for cell in row):
            print('Draw!')
            return
if __name__ == '__main__':
    start()
