from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        to_reach_main: int = 0
        for log in logs:
            if log == '../' and to_reach_main > 0:
                to_reach_main -= 1
            elif log[0] != '.':
                to_reach_main += 1
            print(log,to_reach_main)
        return to_reach_main




if __name__=="__main__":
    s = Solution()

print(s.minOperations(logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))
        