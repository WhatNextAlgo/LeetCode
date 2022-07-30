from more_itertools import padded

def luckyNumbers (matrix):
    lucky_arr = []
    for x in range(len(matrix)):
        min_row = min(matrix[x])
        luckyindex = matrix[x].index(min_row)     
        max_arr = []
        for y in range(len(matrix)):
            max_arr.append(matrix[y][luckyindex])
        if min_row == max(max_arr):
            lucky_arr.append(min_row)

    return lucky_arr



print(luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))