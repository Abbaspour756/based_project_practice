import random
import string
from abc import ABC, abstractmethod  # noqa: F401

import nltk


class PasswordGenerator:
    @abstractmethod
    def generate(self):
        pass

class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length
        
    def generate(self) -> str:
        return ''.join(random.choices(string.digits, k=self.length))
    
class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
        
    def generate(self):
        return ''.join(random.choice(self.characters) for _ in range(self.length))
    
class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self,
                num_of_words: int = 4,
                separator: str = '-', 
                capitalization: bool = False, 
                vocabulary = None
                ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.capitalization = capitalization
        self.separator = separator

    def generate(self):
        password_words = random.choices(self.vocabulary, k=self.num_of_words)
        if self.capitalization:
            password_words = [word.upper() if random.choice((True, False)) else word.lower() for word in password_words]

        return self.separator.join(password_words)
    
if __name__ == '__main__':
    p_obj = RandomPasswordGenerator()
    print(p_obj.generate())