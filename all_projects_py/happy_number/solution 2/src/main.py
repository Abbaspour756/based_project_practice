def is_happy(n: int) -> bool:
    """
    A happy number is defined by the process where you keep replacing the number by the sum of the squares of its digits.
    If this process results in 1, then the number is happy.
    If it loops endlessly in a cycle which does not include 1, then the number is not happy.

    :param n: input number
    :return: the if the number is happy

    examples:
    >>> is_happy(19)
    True
    
    >>> is_happy(2)
    False
    """
    seen_numberss = set()
    while (n != 1) and (n not in seen_numberss):
        seen_numberss.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1

if __name__ == '__main__':
    print(is_happy(int(input("Enter a number: "))))