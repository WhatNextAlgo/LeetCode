from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square
        if not matchsticks:
            return False

        # Number of matchsticks we have
        L = len(matchsticks)

        # Perimeter of our square (if one can be formed)
        perimeter = sum(matchsticks)

        # Possible side of our square.
        possible_side =  perimeter // 4

        # If the perimeter can be equally split into 4 parts (and hence 4 sides, then we move on).
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        matchsticks.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sums = [0 for _ in range(4)]

        # Our recursive dfs function.
        def dfs(index):

            # If we reach the end of matchsticks array, we check if the square was formed or not
            if index == L:
                # If 3 equal sides were formed, 4th will be the same as these three and answer should be True in that case.
                return sums[0] == sums[1] == sums[2] == possible_side

            # The current matchstick can belong to any of the 4 sides (provided their remaining lenghts are >= the size of the current matchstick)
            for i in range(4):
                # If this matchstick can fir in the space left for the current side
                if sums[i] + matchsticks[index] <= possible_side:
                    # Recurse
                    sums[i] += matchsticks[index]
                    print("before dfs",sums)
                    if dfs(index + 1):
                        return True
                    print("after dfs",sums)
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sums[i] -= matchsticks[index]
            return False        
        return dfs(0)

    def makesquare(self, matchsticks):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square.
        if not matchsticks:
            return False

        # Number of matchsticks
        L = len(matchsticks)

        # Possible perimeter of our square
        perimeter = sum(matchsticks)

        # Possible side of our square from the given matchsticks
        possible_side =  perimeter // 4

        # If the perimeter isn't equally divisible among 4 sides, return False.
        if possible_side * 4 != perimeter:
            return False

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):

            # This will calculate the total sum of matchsticks used till now using the bits of the mask.
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[L - 1 - i]

            # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
            if total > 0 and total % possible_side == 0:
                sides_done += 1

            # If we were successfully able to form 3 sides, return True
            if sides_done == 3:
                return True

            # If this recursion state has already been calculated, just return the stored value.
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            # Common variable to store answer from all possible further recursions from this step.
            ans = False

            # rem stores available space in the current side (incomplete).
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            # Iterate over all the matchsticks
            for i in range(L - 1, -1, -1):

                # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
                if matchsticks[L - 1 - i] <= rem and mask&(1 << i):

                    # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                    # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            # cache the result for the current recursion state.            
            memo[(mask, sides_done)] = ans
            return ans

        # recurse with the initial mask with all matchsticks available.
        return recurse((1 << L) - 1, 0)
        

s = Solution()
print(s.makesquare(matchsticks = [1,1,1,1,2,2,2,2,3,3,3,3]))
        