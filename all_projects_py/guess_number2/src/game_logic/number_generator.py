import random


def generate_random_number(start:int, end:int) -> int:
    '''__summary__
    Generates a random number between start and end (inclusive)
    '''
    return random.randint(start, end)