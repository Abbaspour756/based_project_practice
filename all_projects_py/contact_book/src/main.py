from collections import defaultdict


class ContactBook:
    """Manage a collection of contacts with phone numbers and email addresses."""

    def __init__(self):
        """Initialize an empty contact book."""
        # Each contact name maps to a dictionary containing contact details.
        self.contacts = defaultdict(dict)

    def add_contact(self, name, phone_number, email=None):
        """Add a new contact with a name, phone number, and optional email."""
        # Prevent duplicate contacts with the same name.
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
            return

        # Store the contact information in the nested dictionary.
        self.contacts[name]['phone_number'] = phone_number
        self.contacts[name]['email'] = email

    def view_contacts(self):
        """Display all contacts and their details."""
        # Iterate through every contact and its stored details.
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print("_"*50)

    def delete_contact(self, name):
        """Delete a contact by its name."""
        # Check whether the contact exists before deleting it.
        if name in self.contacts:
            del self.contacts[name]
            print('contact deleted successfully')
        else:
            print(f"Contact '{name}' does not exist.")

    def update_contact(self, name, phone_number=None, email=None):
        """Update the phone number and/or email of an existing contact."""
        # Only update the contact if it already exists.
        if name in self.contacts:
            # Update the phone number if a new value was provided.
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number

            # Update the email if a new value was provided.
            if email:
                self.contacts[name]['email'] = email

            print('contact updated successfully')
            return

        print(f"Contact '{name}' does not exist.")


if __name__ == "__main__":
    # Create a ContactBook instance when this file is run directly.
    book = ContactBook()


while True:
    # Display the main menu repeatedly until the user chooses to exit.
    print('\n\nwelcome to contact book')
    print('1. Add contact')
    print('2. View contacts')
    print('3. Delete contact')
    print('4. Update contact')
    print('5. Exit')

    user_choice = input('Enter your choice: ')

    if user_choice == '1':
        # Collect information needed to create a new contact.
        name = input('\nEnter name: ')
        phone_number = input('Enter phone number: ')
        email = input('Enter email: ')
        book.add_contact(name, phone_number, email)

    elif user_choice == '2':
        # Display all contacts stored in the contact book.
        print('\nlist of contacts')
        book.view_contacts()

    elif user_choice == '3':
        # Ask for the name of the contact that should be deleted.
        name = input('Enter name: ')
        book.delete_contact(name)

    elif user_choice == '4':
        # Collect the new information for an existing contact.
        name = input('Enter name: ')
        phone_number = input('Enter new phone number: ')
        email = input('Enter new email: ')

        book.update_contact(name, phone_number, email)

    elif user_choice == '5':
        # Stop the program when the user chooses the exit option.
        print('Thank you for using contact book')
        break

    else:
        # Handle choices that are not part of the menu.
        print('Invalid choice. Please try again.')