def maxArea(height):
    maxval = 0
    left = 0
    right = len(height) -1
    while  left < right:
        width = right - left
        minheight = min(height[left],height[right])
        maxval = max(maxval,minheight * width)

        if height[left]<height[right]:
            left = left + 1
        else:
            right = right -1

    return maxval





lst = [1,8,6,2,5,4,8,3,7]
print(maxArea(lst))