# Happy Number

A simple Python program that checks whether a number is a **Happy Number**.

## What is a Happy Number?

A **Happy Number** is a positive integer that eventually reaches `1` when you repeatedly:

1. Separate the digits of the number.
2. Square each digit.
3. Add the squared digits together.
4. Repeat the process with the new number.

For example:

```text
19
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

Therefore, **19 is a Happy Number**.

## How It Works

The program repeatedly calculates the sum of the squares of the digits until:

* The number becomes `1` → **Happy Number**
* The number enters a cycle → **Not a Happy Number**

## Example

```text
Input: 19

19 → 82 → 68 → 100 → 1

Output:
This is a happy number
```

Another example:

```text
Input: 2

2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...

Output:
This is not a happy number
```

## Project Structure

```text
happy-number/
│
├── main.py
└── README.md
```

## Requirements

* Python 3.x

No external libraries are required.

## Running the Program

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd happy-number
```

Run the program:

```bash
python main.py
```

## Example Happy Numbers

Some Happy Numbers are:

```text
1
7
10
13
19
23
28
31
32
44
49
68
70
79
82
86
91
94
97
100
```

## Concepts Used

This project demonstrates several basic Python concepts:

* Functions
* `while` loops
* `for` loops
* Lists
* Arithmetic operations
* Recursion
* Digit separation
* Conditional statements

## License

This project is for learning and educational purposes.
