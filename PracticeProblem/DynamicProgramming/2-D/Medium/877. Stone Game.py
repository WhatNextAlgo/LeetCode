from typing import List


class Solution:
    # we can directly return True cos Alice always win if she play optimally
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # subarr piles (l,r ) -> Max Alice Total

        #Return : Max Alice Total
        def dfs(l,r):
            if l > r:
                return 0

            if (l,r) in dp:
                return dp[(l,r)]
            
            # We are calculating Alice Total
            # that why we are contributing alice total based in even (bool flag)
            # even is False that's  mean bob is picking and for bob we are not calculating
            # that's why return value is zero
            even =True if (r - l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            # (left pick + left piles)  + (right pick + right piles)
            dp[(l,r)] = max(dfs(l + 1, r) + left ,dfs(l, r-1) + right)

            return dp[(l,r)]

        return dfs(0,len(piles)-1) > (sum(piles)) //2

s = Solution()
print(s.stoneGame(piles = [5,3,4,5]))