def rob(nums):
    length = len(nums) - 1 
    storedMax = 0

    if length < 2:
        storedMax = max(nums[0], nums[1])
        return storedMax

    else:
        for i in range(len(nums) - 2):
            sumNums = nums[i] + nums[i + 2]
            sumMid = nums[i + 1]
            
            storedMax = max(nums[i] + nums[i+2], storedMax)

    # def helper(idx1, idx2):
    #     if idx1 < length or idx2 < length:
    #         return 0
        
    #     sum1 = storedMax + nums[idx1] + nums[idx2]

    #     storedMax = storedMax + max(helper(idx1 + 1), helper(idx2 + 2))
    #     return storedMax

    # return helper(0, 1)

