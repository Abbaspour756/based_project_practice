import random
import string


def random_password():


    length = int(input("Enter the length of the password: "))
    if length < 8:
        print("Password length should be at least 8 characters")
        print('please try again')
        return random_password()

    elif length > 16:
        print("Password length should be at most 16 characters")
        print('please try again')
        return random_password()

    characters = string.ascii_letters + string.digits

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print(f'it is your random password: {password}')


def personal_id_num():
    generate = input("Do you want to generate a random PIN? (yes/no): ")
    if generate.lower() == "yes":
        pin_leg = int(input("Enter the length of the pin: "))
        if pin_leg < 4:
            print("PIN length should be at least 4 characters")
            print('please try again')
            return personal_id_num()

        elif pin_leg > 8:
            print("PIN length should be at most 8 characters")
            print('please try again')
            return personal_id_num()
        
        start = 10 ** (pin_leg - 1)
        end = 10 ** pin_leg - 1
        pin = random.randint(start, end)
        print(f'it is your random pin: {pin}')
    else:
        pin = input("Enter the pin: ")
        if len(pin) < 4:
            print("PIN length should be at least 4 characters")
            print('please try again')
            return personal_id_num()

        elif len(pin) > 8:
            print("PIN length should be at most 8 characters")
            print('please try again')
            return personal_id_num()
    return f'it is your pin: {pin}'
        
        
def memorable_password():
    memo_pass_leg = int(input("how many words do you want in your password?: "))
    memorable_words = ['vignett', 'library', 'franc', 'buckle', 'tornado', 'physic', 'sciense']

    if memo_pass_leg < 2:
        print("password should be at least 2 words")
        print('please try again')
        return memorable_password()
    
    elif memo_pass_leg > 5:
        print("password should be at most 5 words") 
        print('please try again')
        return memorable_password()
    
    main_pass = random.sample(memorable_words, memo_pass_leg)
    print(f'it is your memorable password: {'-'.join(main_pass)}')

def generate_password():
    ask = input("Do you want create which password between [random, memorable, PIN]?: ")
    if ask.lower() == "random":
        random_password()
    elif ask.lower() == "memorable":
        memorable_password()
    elif ask.lower() == "pin":
        personal_id_num()
    else:
        print("your input is unavailable, please try again")
        return generate_password()

if __name__ == "__main__":
    generate_password()
