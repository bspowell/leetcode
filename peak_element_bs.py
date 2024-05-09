
def findPeakElement(nums):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + ((r - l) // 2) # makes sure it doesn't overflow ()
        
        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            l = mid + 1
        elif mid > 0 and nums[mid-1] > nums[mid]:
            r = mid - 1
        else:
            return mid
    return 0



print(findPeakElement([1,2,1,3,5,6,4]))
print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2]))
print(findPeakElement([1,2,3])) 


# class Solution:
#     def findPeakElement(self, nums):
#         """
#         return index of any of the peak elements in nums
#         peak element = element that is greater than both neighbors
#         """
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             mid = (right + left) // 2
#             plusOne = float("-inf") if mid + 1 >= len(nums) else nums[mid + 1]
#             minusOne = float("-inf") if mid - 1 < 0 else nums[mid - 1]

#             if plusOne < nums[mid] and minusOne < nums[mid]:
#                 return mid

#             if nums[mid + 1] > nums[mid]:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return right


# # Tony
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         """
#         - 


#         """ 

#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2
#             a = nums[mid - 1] if (mid - 1) >= 0 else float('-inf')
#             b = nums[mid]
#             c = nums[mid + 1] if (mid + 1) < len(nums) else float('-inf')

#             # increasing
#             if a < b and b < c:
#                 left = mid + 1

#             # decreasing/same
#             elif a < b and b > c:
#                 return mid
#             else:
#                 right = mid - 1
#         return

# # James