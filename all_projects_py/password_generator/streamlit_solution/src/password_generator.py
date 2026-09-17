import random
import string
from abc import ABC, abstractmethod  # noqa: F401

import nltk


class PasswordGenerator:
    """Base class for different types of password generators."""

    @abstractmethod
    def generate(self):
        """Generate and return a password."""


class PinGenerator(PasswordGenerator):
    """Generate a numeric PIN with a specified length."""

    def __init__(self, length: int):
        """Initialize the PIN generator with the desired length."""
        self.length = length

    def generate(self) -> str:
        """Generate a random PIN containing only digits."""
        return ''.join(random.choices(string.digits, k=self.length))


class RandomPasswordGenerator(PasswordGenerator):
    """Generate a random password using letters, numbers, and symbols."""

    def __init__(
        self,
        length: int = 8,
        include_numbers: bool = False,
        include_symbols: bool = False
    ):
        """Initialize the generator with password length and character options."""
        self.length = length

        # Start with uppercase and lowercase letters.
        self.characters = string.ascii_letters

        # Add numbers if requested.
        if include_numbers:
            self.characters += string.digits

        # Add symbols if requested.
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        """Generate and return a random password."""
        return ''.join(
            random.choice(self.characters)
            for _ in range(self.length)
        )


class MemorablePasswordGenerator(PasswordGenerator):
    """Generate a password made from randomly selected words."""

    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-',
        capitalization: bool = False,
        vocabulary = None
    ):
        """Initialize the memorable password generator."""
        # Use the NLTK English word list if no vocabulary is provided.
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.capitalization = capitalization
        self.separator = separator

    def generate(self):
        """Generate a memorable password from random words."""
        # Select the required number of words from the vocabulary.
        password_words = random.choices(
            self.vocabulary,
            k=self.num_of_words
        )

        # Randomly capitalize each word if capitalization is enabled.
        if self.capitalization:
            password_words = [
                word.upper() if random.choice((True, False))
                else word.lower()
                for word in password_words
            ]

        # Join the words using the selected separator.
        return self.separator.join(password_words)


if __name__ == '__main__':
    # Create a default random password generator.
    p_obj = RandomPasswordGenerator()

    # Generate and print a password.
    print(p_obj.generate())