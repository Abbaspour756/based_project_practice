def seprating(number: int) -> list:
    '''This function will return the digits of the number in a list'''
    a = []
    while number > 0:
        digit = number % 10
        number //= 10
        a.append(digit)
    return a


def finder(number: int, count: int = 0) -> str:
    '''This function will find the happy number'''

    if count >= 8:
       return "Stopped after 8 attempts"

    while number != 1:
        num = seprating(number)
        jam = 0
        for i in num:
            jam += i ** 2
        return finder(jam, count + 1)
    return "This is a happy number"

if __name__ == "__main__":
    print(finder(int(input("Enter a number: "))))