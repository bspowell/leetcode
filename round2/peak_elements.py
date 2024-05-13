# binary search
# whichever number is greater move pointer that way
# if left < current num < right, return num
# if left num is greater than mid, move right pointer mid - 1
# if right num is greater than mid, move left pointer mid + 1


def peakElement(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # this ensures the mid point is always in bounds
        mid = left + ((right - left) // 2)
        mval = arr[mid]

        if arr[mid-1] > mval:
            right = mid - 1
        elif arr[mid+1] > mval:
            left = mid + 1
        else: 
            return mid
    


print(peakElement([1,2,3,1]))
print(peakElement([1,2,1,3,5,6,4]))

# 1,2,3,1
# l m   r
# 1,2,3,1
#     l r
#     m
# 1,2,3,1 
# 1,2,3,1 
# 1,2,3,1 