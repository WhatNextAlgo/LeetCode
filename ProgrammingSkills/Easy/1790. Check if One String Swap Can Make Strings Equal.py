class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s2)
        l2 = list(s2)
        i = -1
        j = -1
        for x in range(n):
            if l2[x] != s1[x]:
                if i == -1:
                    i = x
                elif j == -1:
                    j = x
                else:
                    break
                
        l2[i], l2[j] = l2[j],l2[i]
                   
        s2 = "".join(l2)
        if s2 != s1:
            return False
        return True



s = Solution()
print(s.areAlmostEqual(s1 = "siyolsdcjthwsiplccjbuceoxmpjgrauocx", s2 = "siyolsdcjthwsiplccpbuceoxmjjgrauocx"))