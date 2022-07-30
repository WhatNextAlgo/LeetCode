def decode(encoded, first):
    length = len(encoded)
    lst = []
    lst.append(first)
    for x in range(length):
        lst.append(lst[x] ^ encoded[x])

    return lst

print(decode(encoded = [6,2,7,3], first = 4))