def provide_hint(guess:int, actual_number:int) -> str:
    if guess < actual_number:
        return "Your guess is too low"
    elif guess > actual_number:
        return "Your guess is too high"
    else:
        return "Congratulations! You guessed the right number!"
    