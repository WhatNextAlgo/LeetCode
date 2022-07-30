class MinStack:
    
    def __init__(self):
        self.items = []
        self.min_val = 0
    

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.min_val > val:
            self.min_val = val
        

    def pop(self) -> None:
        if self.items != []:
            val = self.items[-1]
            del self.items[-1]
            return val
        

    def top(self) -> int:
        if self.items != []:
            return self.items[-1]

    def getMin(self) -> int:
        if self.items != []:
            return min(self.items)
        

    
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.pop())
print(obj.top())
print(obj.getMin())