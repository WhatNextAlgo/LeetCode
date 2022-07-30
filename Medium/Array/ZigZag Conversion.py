def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            print(lin,s[i])
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows -1:
                    print("in")
                    pl *= -1
        print(outp)
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr

print(convert(s="PAYPALISHIRING",numRows=3))