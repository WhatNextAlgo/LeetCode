class MyHashSet:
    
    def __init__(self):
        self.items = {}
        

    def add(self, key: int) -> None:
        if key not in self.items:
            self.items[key]=key
        

    def remove(self, key: int) -> None:
        if key in self.items:
            del self.items[key]  


    def contains(self, key: int) -> bool:
        return key in self.items
        



obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
obj.remove(2)
print(obj.contains(2))