def removePalindromeSub(s: str) -> int:
    def is_palindrome(s):
        if s == s[::-1]:
            return True
        return False

    if is_palindrome(s):
        return 1
    return 2
print(removePalindromeSub(s = "abb"))