def squareIsWhite(coordinates: str) -> bool:
    if (ord(coordinates[0]) + int(coordinates[1])) % 2 ==0:
        return False
    return True

print(squareIsWhite(coordinates = "c7")) 