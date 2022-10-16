
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len of s1 is greater than len of s2 then No permutation can be formed
        if len(s1) > len(s2):return False 
        s1Count, s2Count = [0] * 26 , [0] * 26  # hashmap with 26 character index

        for i in range(len(s1)): #first window computing
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26): # count the matches after first window computed
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            
            #s2
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1 
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            #remove the left index from the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1 
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26

            
        



s = Solution()
print(s.checkInclusion(s1 = "ab", s2 = "eidboaoo"))