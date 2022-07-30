class CustomStack:
    
    def __init__(self, maxSize: int):
        self.items = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.items) < self.maxSize:
            self.items.append(x)
        

    def pop(self) -> int:
        if self.items != []:    
            return self.items.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        incre_until = k  if len(self.items) > k else len(self.items)
        for x in range(incre_until):
            self.items[x] = self.items[x] + val

        


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(4)
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.items)
print(obj.pop())
obj.push(4)
obj.push(5)
obj.push(6)
obj.push(7)
print(obj.items)
obj.increment(3,100)
print(obj.items)
# obj.increment(2,100)
# print(obj.items)