def firstPalindrome(words):
    for x in words:
        if x == x[::-1]:
            return x
    return ''

print(firstPalindrome( words = ["def","ghi"]))