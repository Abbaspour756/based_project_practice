# Tic-Tac-Toe

A simple, two-player Tic-Tac-Toe game that runs in the terminal. Players take turns placing **X** and **O** on a 3×3 board. The first player to make a row, column, or diagonal wins.

## Requirements

- Python 3
- No third-party packages required

## Run the game

Save the code to a file, such as `tic_tac_toe.py`, then run:

```bash
python tic_tac_toe.py
```

## How to play

The board’s cells are numbered from **1** to **9**:

```text
1|2|3
-----
4|5|6
-----
7|8|9
```

When prompted, enter the number of an empty cell. Players take turns until someone wins or the board is full.

## Notes

- The game currently always starts with **X**.
- The `get_random_first_player()` method is defined but isn’t used by the game.
- Enter a number from 1 to 9. The game does not currently handle non-numeric or out-of-range input.