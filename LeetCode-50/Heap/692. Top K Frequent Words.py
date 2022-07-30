from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for x  in range(len(words) + 1)]
        for x in words:
            count[x] = 1 + count.get(x,0)

        for key,val in count.items():
            freq[val].append(key)
            
        
        res = []
        for i  in range(len(freq)-1,0,-1):
            for n in sorted(freq[i]):
                res.append(n)
                if len(res) == k:
                    return res


s = Solution()
print(s.topKFrequent(["i","love","leetcode","i","love","coding"],3))