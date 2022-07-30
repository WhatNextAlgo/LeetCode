class MyStack:
    
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
 
    def empty(self):
        return self.queue2.is_empty()
 
    def push(self, data):
        self.queue1.enqueue(data)
        while not self.queue2.is_empty():
            x = self.queue2.dequeue()
            self.queue1.enqueue(x)
        self.queue1, self.queue2 = self.queue2, self.queue1
 
    def pop(self):
        return self.queue2.dequeue()

    def top(self):
        return self.queue2.peek()
        
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)

print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.empty())
