# Monty Hall Problem

A simple Python implementation of the **Monty Hall Problem**, a famous probability puzzle based on a game show.

## About the Problem

The game has three doors:

* 🚪 Door 1
* 🚪 Door 2
* 🚪 Door 3

Behind the doors are:

* 🚗 One car
* 🐐 Two goats

The player chooses one door. The host then opens one of the other doors and reveals a goat.

The player is then given a choice:

> Do you want to keep your original door or switch to the remaining unopened door?

The interesting part of the problem is that **switching and staying do not have the same probability of winning**.

## How This Program Works

The program follows these steps:

1. Randomly places one car and two goats behind the three doors.
2. Asks the player to choose a door.
3. Reveals another door containing a goat.
4. Asks whether the player wants to change their choice.
5. Shows the result behind the selected door.

## Example

```text
Choose your door between 1, 2, 3: 2

This door (1) has a goat

Do you want to change your choice? y/n: y

You choose the door 3 and it was a car
```

## Project Structure

```text
monty-hall/
│
├── main.py
└── README.md
```

## Requirements

This project uses only Python's standard library.

No external packages are required.

The program uses:

```python
import random
```

## Running the Program

Make sure Python is installed, then run:

```bash
python main.py
```

The program will ask you to choose a door:

```text
Choose your door between 1, 2, 3:
```

Enter:

```text
1
```

or:

```text
2
```

or:

```text
3
```

Then decide whether you want to switch:

```text
Do you want to change your choice? y/n:
```

Enter:

```text
y
```

to switch or:

```text
n
```

to keep your original choice.

## Main Functions

### `put_randomly()`

Creates the three doors and randomly assigns:

```python
["goat", "car", "goat"]
```

to them.

### `choose_door()`

Handles the player's initial door selection and reveals a goat behind one of the other doors.

### `change_door()`

Handles the final decision of whether the player keeps the original door or switches to the remaining door.

## Technologies

* Python 3
* `random` module
* Dictionaries
* Functions
* Loops
* Conditional statements
* Dictionary methods
* User input

## Note

This project is a basic implementation designed for learning Python and understanding the Monty Hall Problem.

It can be extended to run thousands of simulations and compare the win rates of:

* **Always staying**
* **Always switching**
