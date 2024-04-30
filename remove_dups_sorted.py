# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

# Iterate over the nums array starting at index 1
# if current number is equal to previous, then pop current
# else
#   add to index
# return lenght of array
# Time complexity: O(N) - for iterating over the list only once. 
# space complexity: O(1) - didn't create any new objects or space except count. 

def removeDuplicates(nums):
		i = 1
		while i < len(nums):
			if nums[i] == nums[i - 1]:
				nums.pop(i)
			else:
				i += 1
		return len(nums)

print(removeDuplicates([1,2]))
print(removeDuplicates([0,0,1,1]))
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]


# [1,1,2], k = 0, curr = 1, index = 0, lenghth = 3
# [1,2,_], k = 1, curr = 1, index = 0, length = 2
# [1,2,_], k = 1, curr = 2, index = 2, k = 1
# [0,1,_,_]