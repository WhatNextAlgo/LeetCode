def maximumUniqueSubarray(nums):
    seen = set()
    result = i = total = 0

    for j in range(len(nums)):
        x = nums[j]
        while i < j and x in seen:
            seen.remove(nums[i])
            total -= nums[i]
            i += 1
        
        total += x
        seen.add(x)
        result = max(result,total)
    return result
        


def maximumUniqueSubarray1(nums):
    seen=set() 
    res=i=tot=0
    for j in range(len(nums)):
        x=nums[j]                   
        while i < j and x in seen: 
            seen.remove(nums[i])
            tot-=nums[i]
            i+=1                        
        tot+=x
        seen.add(x)
        res=max(res, tot)            
    return res
print(maximumUniqueSubarray(nums=[4,2,2,5,6]))

print(maximumUniqueSubarray(nums = 
[187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))

