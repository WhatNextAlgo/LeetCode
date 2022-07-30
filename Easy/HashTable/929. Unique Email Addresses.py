from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for _str in emails:
            if "@" in _str:
                local_name,at_sign = _str.split("@")
                if "+" in _str:
                    local_name =  local_name.split("+")[0]
                if "." in _str:
                    local_name = "".join(local_name.split("."))
                
                res.append(local_name +"@"+at_sign)

        return len(set(res))
        


            


        
            

        if "." in _str:
            _str = "".join(_str.split("."))
        


s = Solution()
print(s.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))