class FenwickTree:
    def __init__(self,nums):
        self.nums = nums
        self.fenwick_tree = [0 for _ in range(len(nums) + 1)]


    def construct(self):
        for index in range(1,len(self.nums) + 1):
            self.update(index,self.nums[index-1])

    def range_sum(self,start,end):
        return self.sum(end) - self.sum(start -1)

    def sum(self,index):
        index = index + 1
        total = 0
        while index > 0:
            total += self.fenwick_tree[index]
            index = self.parent(index)
        return total

    def update(self,index,num):

        while index < len(self.nums) + 1:
            self.fenwick_tree[index] += num
            index = self.next(index)

    def next(self,index):
        return index + (index & -index)

    def parent(self,index):
        return index - (index & -index)


if __name__ =="__main__":
    nums = [3,2,-1,6,5,4,-3,3,7,2,3]
    tree = FenwickTree(nums)
    tree.construct()
    print(tree.range_sum(0,2)) 
