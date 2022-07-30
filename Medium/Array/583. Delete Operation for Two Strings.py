def minDistance(word1, word2):
    def getMinDistance(word1,word2):
        m,n=len(word1),len(word2)
        prev=[0] * (m+1)
        
        for i in range(n-1, -1, -1):
            curr=[0] * (m+1)
            for j in range(m-1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j]=1 + prev[j+1]
                else:
                    curr[j]=max(curr[j+1], prev[j])
            prev=curr
            
        return m + n - 2*prev[0]

    if len(word1)>len(word2):
        return getMinDistance(word2,word1)
    return getMinDistance(word1,word2)


# def minDistance(word1, word2):
#     pass




        
print(minDistance(word1 = "sea", word2 = "eat"))
print(minDistance(word1 = "dinitrophenylhydrazine",word2="acetylphenylhydrazine"))