from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubSet(s, subseq):
            l1, l2 = 0, 0
            while l1 < len(s) and l2 < len(subseq):
                # if char is removed then we incr the index of l1 
                # if it is not removed then we check char is match or not  
                if l1 in removed or s[l1] != subseq[l2]: 
                    l1 +=1
                    continue
                # if char match then we incr both the index
                l1 += 1
                l2 += 1
            # if all the char of subseq is present then l2 should be equal to len of subseq
            return l2 == len(subseq)  
        res = 0
        l, r = 0, len(removable) -1
        while l <= r:
            m = l + ((r - l)//2)
            removed = set(removable[:m + 1])
            if isSubSet(s,p):
                res = max(res,m + 1)
                l = m + 1
            else:
                r = m - 1
        return res


s = Solution()
print(s.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))