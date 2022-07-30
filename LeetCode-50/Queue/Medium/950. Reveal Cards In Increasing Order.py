import collections
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,x:int):
        self.items.append(x)

    def dequeue(self) ->int :
        if not self.is_empty():
            return self.items.pop(0)
    def is_empty(self):
        return self.items == []


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        index = Queue()
        for x in range(n):
            index.enqueue(x)

        ans = [None] * n

        for card in sorted(deck):
            ans[index.dequeue()] = card
            if index:
                index.enqueue(index.dequeue())

        return ans


s = Solution()
print(s.deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]))