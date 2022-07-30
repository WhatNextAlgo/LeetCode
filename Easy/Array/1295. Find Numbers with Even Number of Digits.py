def findNumbers(nums):

    def digit_count(n):
        count = 0
        while n > 0:
            d1 = n//10
            n = d1
            count +=1
        return count

    count = 0
    for x in nums:
        if digit_count(x) % 2 == 0:
            count +=1

    return count

print(findNumbers(nums = [555,901,482,1771]))
