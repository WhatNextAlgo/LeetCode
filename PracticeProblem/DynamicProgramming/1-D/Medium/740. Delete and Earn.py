from typing import Counter, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1 , earn2 = 0,0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            #can't use both curEarn and earn2
            if i > 0 and nums[i] == nums[i-1] + 1: # 4 ==  3 + 1
                # changing pointer to earn2 --> earn1 and earn2 --> new index
                temp = earn2
                earn2 = max(curEarn + earn1,earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp

        return earn2



s = Solution()
print(s.deleteAndEarn(nums = [2,2,3,3,3,4]))