# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#  
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Given an array
# - iterate over it using indexes
# - multiply every nnumber 
# - for every left pointer starting at 0, right starting at 1
# - take  

def productExceptSelf(nums):
    result = []
    
    for i in range(len(nums)):
        sum = 1
        popped = nums.pop(i)
        for l in range(len(nums)):
            sum *= nums[l]

        result.append(sum)
        nums.insert(i, popped)
    return result



print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
# print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
# print(productExceptSelf([1,2,0,0])) # 