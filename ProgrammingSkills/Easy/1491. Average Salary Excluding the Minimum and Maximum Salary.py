from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        max_val = min_val= total= salary[0]
        n = len(salary)
        for x  in range(1,len(salary)):
            total += salary[x]
            if salary[x] < min_val:
                min_val = salary[x]
            elif salary[x] > max_val:
                max_val = salary[x]

        return (total - (max_val + min_val))/(n-2)


s = Solution()
print(s.average(salary = [4000,3000,1000,2000]))