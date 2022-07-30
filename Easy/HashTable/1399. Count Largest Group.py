class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_count(num):
            count = 0
            while num > 0:
                val = num % 10
                num = num//10
                count += val
            return count
        d = {}
        for  x in range(1,n+1):
            if digit_count(x) in d:
                d[digit_count(x)] += 1
            else:
                d[digit_count(x)] = 1
        max_val = max(d.values())
        return list(d.values()).count(max_val)

            


s = Solution()
print(s.countLargestGroup(n = 2))