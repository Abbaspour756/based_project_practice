def get_valid_input(prompt: str,start , end):
    while True:
        try:
            user_input = int(input(prompt))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Please enter a number between {start} and {end}")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    print(get_valid_input("Enter a number between 1 and 10: ",1,10))