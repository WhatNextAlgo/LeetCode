class NestedIterator:
    def __init__(self, nestedList):
        #Using a stack of [list, index] pairs. index is the pointer of the current elem in one nested list
        self.stack = [[nestedList,0]]
        
    
    def next(self) -> int:
        self.hasNext()
        # we read in the current nestedlist and its current index
        nested_list, i = self.stack[-1]
        # now that we will return the current value in this list, we move index forward.
        self.stack[-1][1] += 1
        return nested_list[i].getInteger()
        
    
    def hasNext(self) -> bool:
        s =self.stack # just for being easy to read
        while s:
            # while we still have list to check, return the current nest and its current index
            nested_list, i = s[-1]
            # if this happens, it means the index has already go through every elem in the current nestlist, so we pop this list out, then try to see if we have a next nestedlist (go back to while)
            if i == len(nested_list):
                s.pop()
            # if the index is not in the end of list, we extract what index points at to x, and check if x is a pure value of another list. If it is int, it means we have next value for iteration, so hasNext returns True
            #if x is another list, then we firstly move the index forward, because we have checked the current element, and we push a new nestedlist into stack, we will check it from 0 index, until we see a int value and return True.
            else:
                x = nested_list[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(),0])
        # if stack is empty, we reach the end of entire nestedlist, so we return False
        return False
