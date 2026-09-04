from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import generate_random_number
from src.utils.input_validator import get_valid_input


def main():
    score = 100
    actual_number = generate_random_number(1, 100)

    while True:
        guess = get_valid_input("Enter your guess: ", 1, 100)
        hint = provide_hint(guess, actual_number)
        print(hint)
        score -= 5
        print(f"Your score is {score}")
        if guess == actual_number:
            print(f"Congratulations! You guessed the number in {score} attempts.")
            break

if __name__ == "__main__":
    main()
