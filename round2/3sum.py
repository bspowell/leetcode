# array of nums
# return all triplets of unique values that equal  = 0 

# sort array
# iterate over the array and have two pointers
# iteration will start at 0, and left pointer will start + 1, right pointer index -1
# start = 0, left = start + 1, right = -1
# if start - 1 == start
#   continue
# while left < right
    # if sum == 0
    #   add numbers to result array
    #   break
    # if left pointer < right pointer and sum < k
    #   then move left pointer up
    # elif left pointer < right pointer and sum > k:  (sum is greater than k )
    #   move right pointer back one, since sum is greater
# 

# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]
#  s  l         r
# [-4,-1,-1,0,1,2]
#  s     l      r
# [-4,-1,-1,0,1,2]
#  s        l   r
# [-4,-1,-1,0,1,2]
#  s  l       l r
# [-4,-1,-1,0,1,2]
#      s  l     r
#      [-1, -1, 2] added to result array
# [-4,-1,-1,0,1,2]
#         s 1   r

# [0,0,0,0]
# 


def threeSum(nums):
    result = [] 
    nums.sort()

    for start in range(len(nums) - 2):
        left = start + 1
        right = len(nums) - 1
        
        # if previous start number is the same
        if start > 0 and nums[start] == nums[start - 1]:
            continue
        while left < right:
            summ = nums[start] + nums[left] + nums[right]
            if summ == 0:
                result.append([nums[start], nums[left], nums[right]])
                left += 1
                # if previous left pointer num is the same, continue until different num
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif summ < 0:
                left += 1
            else: 
                right -= 1


    return result


print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,0,0,0]))