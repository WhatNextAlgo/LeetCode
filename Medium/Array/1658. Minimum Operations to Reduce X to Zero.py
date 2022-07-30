def minOperations(nums, x):
    target = sum(nums) - x
    curr_sum, max_len = 0, 0
    start = 0
    found = False
    for end in range(len(nums)):
        curr_sum += nums[end]
        print("C ",curr_sum)
        while start <= end and curr_sum > target:
            curr_sum -= nums[start]
            start += 1
        if curr_sum == target:
            found = True
            max_len = max(max_len, end - start + 1)

    return len(nums) - max_len if found else -1



print(minOperations(nums = [3,2,20,1,1,3], x = 10))

            

        