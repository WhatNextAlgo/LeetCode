class RecentCounter:
    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
                self.queue.pop(0)
        return len(self.queue)
                

            
if __name__=="__main__":
    
    obj = RecentCounter()
    print(obj.ping(642))
    print(obj.ping(1849))
    print(obj.ping(4921))
    print(obj.ping(5936))
    print(obj.ping(5957))
    print(obj.queue)

["RecentCounter","ping","ping","ping","ping","ping"]
[[],[642],[1849],[4921],[5936],[5957]]