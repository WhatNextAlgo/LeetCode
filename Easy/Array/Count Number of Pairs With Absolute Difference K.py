
def countKDifference(nums, k):
    apps = {}
    for num in nums:
        if num - k not in apps:
            apps[num-k] = 1
        else:
            apps[num-k] +=1
    count = 0
    for i in range(len(nums)):
        if nums[i] in apps:
            count += apps[nums[i]]
    return count

print(countKDifference(nums = [1,2,2,1], k = 1))
