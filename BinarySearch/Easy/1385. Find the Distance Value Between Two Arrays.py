class Soltution:
    def binary_search(self,arr,start,end,key):
        if start > end:
            return start
        
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            return self.binary_search(arr, mid+1, end, key)
        else:
            return self.binary_search(arr, start, mid-1, key)

    def findTheDistanceValue(self,arr1, arr2, d):
        arr2.sort()
        count = 0
        for key in arr1:
            index = self.binary_search(arr2,0,len(arr2)-1,key)
            # index will store the element which is greater or equal to elem
            print('for key {}, index {}'.format(key, index))
            if index < len(arr2) and abs(key - arr2[index]) <=d or (index -1 >=0 and abs(key - arr2[index-1]) <=d):
                print('inside for key {}, index {}'.format(key, index))
                continue
            else:
                count += 1
        return count

                


s = Soltution()

print(s.findTheDistanceValue(arr1 = [1,4,2,3], arr2 =  [-4,-3,6,10,20,30], d = 3))