# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.
 
# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# Example 2:

# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.
# Example 3:

# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]

# input: array, difference amount
# output: Return number of pairs with difference k
# DSA:
# Interate over the array, then used a nested for loop to interate index + 1, if first array num -/+ k equals second array num, +1 to pairs
# returns pairs count
# Time Complexity: Nested iterating over the array, O(N^2)
# Space Complexity: No additional space taken up besides pairs variable - O(1)

  
def countKDifference(nums, k):
    pairs = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] - k) == nums[j] or (nums[i] + k) == nums[j]:
              pairs += 1
    return pairs


print(countKDifference([1,2,2,1], 1)) #4