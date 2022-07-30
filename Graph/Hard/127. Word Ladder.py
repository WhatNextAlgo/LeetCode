import collections
from typing import List



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern  =  word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
                print(nei)
        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word= q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0

s = Solution()
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))127. Word Ladder.py
