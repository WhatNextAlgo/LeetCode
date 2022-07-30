def smallerNumbersThanCurrent(nums):
    lst = []
    for x in nums:
        count = 0
        for y in nums:
            if x > y:
                count +=1

        lst.append(count)
    return lst

print(smallerNumbersThanCurrent([7,7,7,7]))