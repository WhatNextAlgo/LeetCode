from more_itertools import last


def longestPalindrome(s: str):
    n = len(s)
    if n < 2:
        return s
    
    start = 0
    max_length = 1
    for x in range(n):
        
        low = x -1
        high = x + 1
        print("f ",x)
        print("f ",low,high)
        while (high < n and s[high] == s[x]):
            print("wh ",high)
            high = high + 1

        while (low >= 0 and s[low] == s[x]):
            print("wl ",low)
            low = low -1

        while (low >= 0 and high < n and s[low] == s[high]):
            print("l -",low)
            print("h -",high)
            low = low - 1
            high = high + 1
        print("---")
        length = high - low -1
        if max_length < length:
            max_length = length
            start = low + 1

    return s[start:start + max_length]
            

    


print(longestPalindrome(s = "babad"))