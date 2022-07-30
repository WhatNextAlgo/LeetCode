def kidsWithCandies(candies, extraCandies):
    maxval = max(candies)
    return [ True if x + extraCandies >= maxval else False for x in candies  ]

print(kidsWithCandies([4,2,1,1,2],1))