import random

num = random.randint(1, 100)
person_num = input("Guess a number between 1 and 100: ")
core = 10

while core > 0:
    if person_num == "quit":
        print("You quit the game.")
        break
    elif int(person_num) == num:
        print("You guessed the correct number!")
        break
    elif int(person_num) > num:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    core -= 1
    print(f"You have {core} guesses left.\n")
    print('if you want to quit the game type "quit"\n\n')
    person_num = (input("Guess again: "))