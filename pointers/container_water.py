# Given integer array height of length n
# n = number of vertical lines drawn and how far down x axis
# height = y axis, how high the lines go
# eg. [1,8,6]
# x axis = 1,2,3 
# y axis = 1,8,6
# container = x axis (r - l) * y axis 
def maxArea(height):
    r = len(height) - 1
    l = 0
    vol = 0

    while l < r:
        minH = min(height[l], height[r])
        vol = max(minH * (r-l), vol)
        if height[r] > height[l]:
            l += 1
        else: 
            r -= 1
    return vol




print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 49
print(maxArea([1,2,1]))
