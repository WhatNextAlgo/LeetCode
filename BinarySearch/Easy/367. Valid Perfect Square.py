from math import floor


def isPerfectSquare(num):
    val = floor(num ** 0.5) ** 2
    if val == num:
        return True
    return False

print(isPerfectSquare(num=9))