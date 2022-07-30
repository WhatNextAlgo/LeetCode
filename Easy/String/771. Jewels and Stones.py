def numJewelsInStones(jewels: str, stones: str) -> int:
    total = 0
    for x in jewels:
        if x in stones:
            total += stones.count(x)
    return total

print(numJewelsInStones(jewels = "z", stones = "ZZ"))