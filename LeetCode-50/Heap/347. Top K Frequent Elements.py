from typing import List


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        lst = sorted(d.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in lst[:k]]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x  in range(len(nums) + 1)]
        for x in nums:
            count[x] = 1 + count.get(x,0)

        for key,val in count.items():
            freq[val].append(key)
            
        
        res = []
        for i  in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



s = Solution()
print(s.topKFrequent(nums = [1,2], k = 2))
