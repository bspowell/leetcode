def findMin(nums):
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
        mid = l + ((r-l) // 2)
        
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
    
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
        
    return -1


print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11

#tony

# def findMin(self, nums: List[int]) -> int:
#     """
#     possibilities
#     L < M and R < M

#     [5:L   1     2:M   3     4:R]
#     [5:LM  1:R   2     3     4]
#     [5     1:LMR 2     3     4]
#     [5     1     2     3     4]
#     [5     1     2     3     4]
#     [5,1,2,3,4]
#     [5,1,2,3,4]
#     """

#     left, right = 0, len(nums) - 1
#     lowest = float('inf')

#     while left <= right:
#         mid = (left + right) // 2
#         lowest = min(nums[mid], lowest)

#         left_val, right_val = nums[left], nums[right]

#         if left_val > right_val and nums[mid] >= right_val:
#             left = mid + 1
#         else:
#                 right = mid - 1


# # garret
# class Solution:
#     def findMin(self, nums):
#         left = 0
#         right = len(nums) - 1
#         minNum = float("inf")

#         while left <= right:
#             mid = (left + right) // 2
#             # print(left, mid, right)
#             minNum = min(minNum, nums[mid])

#             # e.g. [3, 4, 5, 1, 2]
#             if nums[left] > nums[right] and nums[left] < nums[mid]:
#                 left = mid + 1
#             # e.g. [5, 1, 2, 3, 4]
#             elif nums[left] > nums[right] and nums[left] > nums[mid]:
#                 right = mid - 1
#             # e.g. [1, 2, 3, 4, 5]
#             elif nums[left] < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         return minNum