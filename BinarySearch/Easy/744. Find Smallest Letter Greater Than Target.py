def nextGreatestLetter(letters, target):
    start = 0
    end = len(letters) -1
    ans = letters[0]
    while start <= end:
        mid = (start + end)//2
        if letters[mid] >  target:
            end = mid -1
            ans = letters[mid]
            
        else:
            start = mid + 1
            

    return ans

def nextGreatestLetter1(letters, target):
    l=0
    r=len(letters)-1
    res=letters[0]
    while(l<=r):
        mid=(l+r)//2
        if letters[mid]>target:
            r=mid-1
            res=letters[mid]
        else:
            l=mid+1
    return res


print(nextGreatestLetter(letters = ["c","f","j"], target = "j"))