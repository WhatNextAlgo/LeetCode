def lengthOfLongestSubstring(s: str):
    last_seen = {}
    l = 0
    max_length = 0
    for x in range(len(s)):
        if s[x] in last_seen:
            l = max(last_seen[s[x]],l)
        last_seen[s[x]] = x + 1 
        max_length = max(max_length,x-l + 1)
    
    return max_length



print(lengthOfLongestSubstring(s = "dvdf"))
