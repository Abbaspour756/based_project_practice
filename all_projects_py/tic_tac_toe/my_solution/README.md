# Tic-Tac-Toe

A simple **Tic-Tac-Toe** game written in Python.

The game is played by two players:

* **Player O** uses `O`
* **Player X** uses `X`

Players take turns selecting cells on a 3×3 board.

## Features

* 3×3 Tic-Tac-Toe board
* Two-player gameplay
* Player O and Player X
* Cell selection using numbers from 1 to 9
* Prevents players from placing a symbol in an occupied cell
* Detects some winning conditions
* Detects a draw when all cells are occupied
* Uses a Python class to manage the game board

## Board

The cells are numbered conceptually like this:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

For example, choosing:

```text
player O, choose a cell: 5
```

places `O` in the center:

```text
[' ', ' ', ' ']
[' ', 'O', ' ']
[' ', ' ', ' ']
```

## How It Works

### `TicTacToe`

The `TicTacToe` class stores and manages the game board.

### `__init__()`

Creates an empty 3×3 board:

```python
self.board = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]
```

### `show_board()`

Prints the current board to the console.

### `circle()`

Handles the move for player `O`.

The player enters a number from `1` to `9`. The number is converted into a row and column:

```python
row = (target - 1) // 3
col = (target - 1) % 3
```

If the selected cell is empty, `O` is placed there.

### `cross()`

Works similarly to `circle()`, but places `X` for player X.

### `start()`

Creates the game and controls the main game loop.

The game:

1. Creates an empty board.
2. Displays the board.
3. Lets player O make a move.
4. Lets player X make a move.
5. Checks for a win.
6. Checks for a draw.
7. Continues until the game ends.

## Running the Game

Make sure Python is installed.

Save the code in a file such as:

```text
tic_tac_toe.py
```

Then run:

```bash
python tic_tac_toe.py
```

## Example

```text
[' ', ' ', ' ']
[' ', ' ', ' ']
[' ', ' ', ' ']

player O, choose a cell: 1

['O', ' ', ' ']
[' ', ' ', ' ']
[' ', ' ', ' ']

player X, choose a cell: 5
```

## Concepts Practiced

This project is useful for practicing:

* Classes
* Objects
* `__init__`
* Instance attributes
* Methods
* Lists
* Nested lists
* `if` statements
* `while` loops
* Functions
* User input
* Recursion
* Boolean variables
* `all()`
* The `__name__ == '__main__'` pattern

## Note

This version intentionally keeps the original game logic. The win-checking section currently checks specific winning conditions for player `O`; it can be expanded later to check all rows, columns, diagonals, and both players.

```
```
