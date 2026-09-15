import random
import string


def random_password():
    """Generate a random password containing letters and digits."""

    while True:
        # Get the password length from the user
        length = int(input("Enter the password length: "))

        if 8 <= length <= 16:
            break

        print("Password length must be between 8 and 16 characters.")
        print("Please try again.")

    # Use letters and digits as possible password characters
    characters = string.ascii_letters + string.digits

    # Generate a random password with the selected length
    password = "".join(random.choice(characters) for _ in range(length))

    print(f"Your random password: {password}")


def personal_id_num():
    """Generate a random PIN or validate a user-provided PIN."""

    generate = input("Do you want to generate a random PIN? (yes/no): ")

    if generate.lower() == "yes":
        while True:
            # Get the desired PIN length
            length = int(input("Enter the PIN length: "))

            if 4 <= length <= 8:
                break

            print("PIN length must be between 4 and 8 characters.")
            print("Please try again.")

        # Generate a PIN with the requested number of digits
        pin = random.randint(10 ** (length - 1), 10 ** length - 1)

    else:
        while True:
            # Let the user enter their own PIN
            pin = input("Enter the PIN: ")

            if 4 <= len(pin) <= 8:
                break

            print("PIN length must be between 4 and 8 characters.")
            print("Please try again.")

    print(f"Your PIN: {pin}")


def memorable_password():
    """Generate a memorable password using randomly selected words."""

    # Words that can be used to create the password
    words = [
        "vignett",
        "library",
        "franc",
        "buckle",
        "tornado",
        "physic",
        "sciense",
    ]

    while True:
        # Get the number of words for the password
        length = int(input("How many words do you want in your password?: "))

        if 2 <= length <= 5:
            break

        print("Password should contain between 2 and 5 words.")
        print("Please try again.")

    # Select unique random words and join them with hyphens
    password = "-".join(random.sample(words, length))

    print(f"Your memorable password: {password}")


def generate_password():
    """Ask the user which type of password they want to create."""

    while True:
        # Ask the user to choose a password type
        password_type = input(
            "Which password do you want to create "
            "[random, memorable, PIN]?: "
        ).lower()

        if password_type == "random":
            random_password()
            break

        if password_type == "memorable":
            memorable_password()
            break

        if password_type == "pin":
            personal_id_num()
            break

        print("Invalid input. Please try again.")


if __name__ == "__main__":
    generate_password()