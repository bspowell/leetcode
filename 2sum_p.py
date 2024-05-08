# use a hash, store all elemnets in the array in the hash with indexes
# iterate over the array and check if current element and target - current element is in hash
# if it is, return indecies

def twoSum(nums, target):
    hash = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in hash:
            return [hash[complement], i]
        hash[nums[i]] = i

    return []  

print(twoSum([2,7,11,15], 9))
print(twoSum([3, 3], 6))
print(twoSum([3, 2, 4], 6))
