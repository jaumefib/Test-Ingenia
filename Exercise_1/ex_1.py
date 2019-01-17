

def get_digit(n, p):
    """
    :param n:  number from which we want to obtain the digit
    :param p:  index of the position of the digit that we want.
    Positions are counted starting in one and from the right to the left
    :return: returns de digit of the number n in the p position
    """
    return n // 10**(p-1) % 10


def enter_numbers():
    """
    :return: Returns the given non empty sequence of natural numbers into a list
    """
    n = int(input("Enter the length of the list: "))
    l = []
    while n > 0:
        elem = input("Enter the number: ")
        l.append(int(elem))
        n = n - 1
    return l


def valencia(x):
    """
    :param x: number of which we want to obtain the valencia
    :return: the valencia of the number
    """
    odd = 0
    even = 0
    n = len(str(x))
    i = 1
    while i <= n:
        v = get_digit(x, i)
        if i % 2 == 0:
            even = even + v
        else:
            odd = odd + v
        i = i + 1
    return abs(odd - even)


if __name__ == "__main__":
    numbers = enter_numbers()
    greatest_val = 0
    b = 0  # Boolean: true if there is a balanced number in the list; false otherwise.
    for x in numbers:
        res = valencia(x)
        if res == 0:
            print("Number "+str(x)+" is balanced")
            b = 1
            break
        elif res > greatest_val:
            greatest_val = res
    if not b:
        print("There is not any balanced number")
        print("The greatest valencia of the numbers in the sequence is: "+str(greatest_val))
