class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # last row
        # last row has been calculate above so will iterate m-1
        for i in range(m-1):
            newRow = [1] * n 
            for j in range(n - 2,-1,-1):
                newRow[j] = newRow[j + 1] + row[j] # right value, down value
            row = newRow
        return row[0]
s = Solution()
print(s.uniquePaths(m = 3, n = 7))
print(s.uniquePaths( m = 3, n = 2))