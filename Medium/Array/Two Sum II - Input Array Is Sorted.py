def twoSum(numbers, target):
    i = 0
    j = len(numbers)-1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            return [i + 1, j + 1]
        
        if s > target:
            j -= 1
        else:
            i += 1

    return [] 


print(twoSum(numbers = [-1,0], target = -1))