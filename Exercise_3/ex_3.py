
def myLength(L):
    """
    :param L: a list
    :return: the length of the list
    """
    res = 0
    for _ in L:
        res += 1
    return res  # or also len(L)


def myMaximum(L):
    """
    :param L: a non-empty list
    :return: the maximum of the list
    """
    maximum = L[0]
    for i in L:
        if maximum < i:
            maximum = i
    return maximum


def average(L):
    """
    :param L: non-empty list of numbers
    :return: the average of the list
    """
    sum = 0
    size = 0
    for i in L:
        sum += i
        size += 1
    return sum / size  # or also sum(L)/len(L)


def buildPalindrome(L):
    """
    :param L: a list
    :return: the palindrome that starts
    with the reverse of the list
    """
    res = []
    aux = L[:]
    for _ in range(len(L)):
        res.append(L.pop())
    return res + aux


def remove(L1, L2):
    """
    :param L1: a list
    :param L2:  a list
    :return: the list L1 after removing the occurences
    of the elements in L2
    """
    #L1.sort()
    #L2.sort()
    for x in L1:
        for y in L2:
            if x == y:
                L1.remove(x)
                break
    return L1


def flatten(L):
    """
    :param L: a list
    :return: the listed flattened
    """
    res = []
    for elem in L:
        if isinstance(elem, list):
            aux = flatten(elem)
            res += aux
        else:
            res.append(elem)
    return res


def oddsNevens(L):
    """
    :param L: a list of integers
    :return: two lists, one with all the odd numbers
    and one with all the even numbers, in the same relative
    order than the original
    """
    odd = []
    even = []
    for elem in L:
        if elem % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
    return odd, even


def primedivisors(n):
    """
    :param n: non-zero positive integer
    :return: the list of all prime divisors of n
    """
    res = []
    b = 0
    for div in range(2, n):
        if n % div == 0:
            b = 1
            res.append(div)
            n = n / div
    if not b:
        res.append(n)
    return res


def get_digit(n, p):
    """
    :param n:  number from which we want to obtain the digit
    :param p:  index of the position of the digit that we want.
    Positions are counted starting in one and from the right to the left
    :return: returns de digit of the number n in the p position
    """
    return n // 10**(p-1) % 10


def number_increase(num):
    """
    :param num: integer
    :return: True if every digit of the number is less than or equal
    to the digit which is on its right (if any), False otherwise
    """
    i = 2
    prev = get_digit(num, 1)
    while i <= len(str(num)):
        v = get_digit(num, i)
        if v > prev:
            return False
        prev = v
        i += 1
    return True


def is_increasing(L):
    """
    :param L: a list of integers
    :return: a list of booleans
    """
    res = []
    for elem in L:
        res.append(number_increase(elem))
    return res

####################################################
#                 Test examples                    #
####################################################


if __name__ == "__main__":
    print("--------- myLength -----------")
    print("myLength([2, 3, 6, 10])")
    print(str(myLength([2, 3, 6, 10])))
    print("myLength([])")
    print(str(myLength([])))

    print("--------- myMaximum ----------")
    print("myMaximum([14, 3, 11, 5, 24, 9, 2])")
    print(str(myMaximum([14, 3, 11, 5, 24, 9, 2])))
    print("myMaximum([10, 10, 10, 10])")
    print(str(myMaximum([10, 10, 10, 10])))

    print("---------- average -----------")
    print("average([1, 2, 3, 4, 5])")
    print(str(average([1, 2, 3, 4, 5])))
    print("average([10, 10, 10, 10])")
    print(str(average([10, 10, 10, 10])))

    print("------ buildPalindrome -------")
    print("buildPalindrome(['fish', 'and', 'chips'])")
    print(str(buildPalindrome(['fish', 'and', 'chips'])))
    print("buildPalindrome([])")
    print(str(buildPalindrome([])))

    print("----------- remove -----------")
    print("remove([1, 2, 3, 4, 5, 6],[2, 4, 6])")
    print(str(remove([1, 2, 3, 4, 5, 6], [2, 4, 6])))
    print("remove([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[10, 4, 32, 23, 14, 5, 63, 64])")
    print(str(remove([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 4, 32, 23, 14, 5, 63, 64])))
    print("remove([1, 2, 3, 4],[]")
    print(str(remove([1, 2, 3, 4], [])))
    print("remove([], [1, 2, 3, 4]")
    print(str(remove([], [1, 2, 3, 4])))

    print("----------- flatten ----------")
    print("flatten([2, ['hello', 'good'], [2.0, 5.5, 10]])")
    print(str(flatten([2, ['hello', 'good'], [2.0, 5.5, 10]])))
    print("flatten([[[4, 2, 1], [3, 'well done']], [[], [1], [0], [[]]]])")
    print(str(flatten([[[4, 2, 1], [3, 'well done']], [[], [1], [0], [[]]]])))

    print("--------- oddsNevens ---------")
    print("oddsNevens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])")
    print(str(oddsNevens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print("oddsNevens([13, 21, 32, 45, 58, 64, 73, 81, 95, 106])")
    print(str(oddsNevens([13, 21, 32, 45, 58, 64, 73, 81, 95, 106])))
    print("oddsNevens([])")
    print(str(oddsNevens([])))

    print("------- primedivisors --------")
    print("primedivisors(255)")
    print(str(primedivisors(255)))
    print("primedivisors(17)")
    print(str(primedivisors(17)))

    print("------- is_increasing --------")
    print("is_increasing([1234, 4321, 36788, 12341])")
    print(str(is_increasing([1234, 4321, 36788, 12341])))
    print("is_increasing([])")
    print(str(is_increasing([])))
