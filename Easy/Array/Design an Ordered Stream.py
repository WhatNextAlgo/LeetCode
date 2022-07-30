class OrderedStream:
    
    def __init__(self, n: int):
        self.storage = {}
        self.i = 1
        

    def insert(self, idKey, value):
        self.storage[idKey] = value
        res = []
        while self.i in self.storage:
            res.append(self.storage[self.i])
            self.i += 1
        
        return res

obj = OrderedStream(5)
param3 = obj.insert(3,"ccccc")
print(param3)
param2 = obj.insert(1,"aaaaa")
print(param2)
param4 = obj.insert(2,"bbbbb")
print(param4)
param5 = obj.insert(5,"eeeee")
print(param5)
param6 = obj.insert(4,"ddddd")
print(param6)
print(obj.storage)




