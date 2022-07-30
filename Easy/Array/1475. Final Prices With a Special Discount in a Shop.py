def finalPrices(prices):
    length = len(prices)
    lst =[]
    for x in range(length):
        for y in range(x + 1, length):
            if prices[x] >= prices[y]:
                lst.append(prices[x]-prices[y])
                break
        else:
            lst.append(prices[x])

    return lst

print(finalPrices(prices = [8,4,6,2,3]))