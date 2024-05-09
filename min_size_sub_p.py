def minSubArrayLen(target, nums):
    l, total = 0, 0
    res = float('inf')

    for r in range(len(nums)):
        total += nums[r]
        while total >= target: # this will keep going until
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1
    
    return 0 if res == float('inf') else res 

print(minSubArrayLen(7, [2,3,1,2,4,3]))


    # l, r = 0, len(arr) - 1
    
    # while l <= r:
    #     mid = (l + r) // 2
        
    #     # Check if the target is equal to the middle element
    #     if arr[mid] == target:
    #         return mid
        
    #     # If the target is less than the middle element, search in the l half
    #     elif target < arr[mid]:
    #         r = mid - 1
        
    #     # If the target is greater than the middle element, search in the r half
    #     else:
    #         l = mid + 1
    
    # # Target not found in the array
    # return -1