def threeSum(nums):
    lst = []
    length = len(nums)
    for x in range(length):
        for y in range(x + 1,length):
            for z in range(y + 1,length):
                l = sorted([nums[x] , nums[y] , nums[z]])
                if (nums[x] + nums[y] + nums[z]) == 0:
                    lst.append(l)

    return lst

    


lst = [-1,0,1,2,-1,-4]

print(threeSum(lst))

