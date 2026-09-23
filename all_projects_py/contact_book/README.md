# Contact Book

A simple command-line contact book application written in Python. It allows users to add, view, update, and delete contacts using an interactive menu.

## Features

* Add a new contact
* View all contacts
* Delete a contact
* Update a contact's phone number or email
* Prevent duplicate contact names
* Handle contacts using nested dictionaries
* Use `defaultdict` to manage contact data

## How It Works

Each contact is stored using the contact's name as the key.

The contact information is stored in a nested dictionary:

```python
{
    "Ali": {
        "phone_number": "123456789",
        "email": "ali@example.com"
    }
}
```

The program uses `defaultdict(dict)` to create the nested dictionaries automatically.

## Menu

When the program starts, it displays the following menu:

```text
1. Add contact
2. View contacts
3. Delete contact
4. Update contact
5. Exit
```

The user selects an option by entering its number.

## Example

Adding a contact:

```text
welcome to contact book

1. Add contact
2. View contacts
3. Delete contact
4. Update contact
5. Exit

Enter your choice: 1

Enter name: Ali
Enter phone number: 123456789
Enter email: ali@example.com
```

Viewing contacts:

```text
list of contacts

Name: Ali
Phone Number: 123456789
Email: ali@example.com
__________________________________________________
```

## Technologies

* **Python 3**
* `collections.defaultdict`

No external packages are required.

## Running the Project

Make sure Python is installed on your computer.

Run the program from the terminal:

```bash
python contact_book.py
```

## Project Structure

```text
contact-book/
│
├── contact_book.py
└── README.md
```

## Concepts Practiced

This project is useful for practicing several Python concepts:

* Classes and objects
* `__init__`
* Methods
* Dictionaries
* Nested dictionaries
* `defaultdict`
* `if` / `elif` / `else`
* `while` loops
* `for` loops
* User input
* String formatting with f-strings
* The `__name__ == "__main__"` pattern
* Basic CRUD operations

## CRUD Operations

The application follows the basic CRUD concept:

| Operation | Function           |
| --------- | ------------------ |
| Create    | `add_contact()`    |
| Read      | `view_contacts()`  |
| Update    | `update_contact()` |
| Delete    | `delete_contact()` |

## Requirements

Python 3.x

No additional dependencies are required.

## License

This project is for learning and educational purposes.

```
```
