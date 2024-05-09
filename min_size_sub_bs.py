class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Check if sliding window of k is above target, return True or False
        def isSumInLength(k):
            window_sum = 0

            for runner in range(len(nums)):
                window_sum += nums[runner]
                if runner > k - 1:
                    window_sum -= nums[runner - k]
                
                if window_sum >= target:
                    return True
            return False

        left, right = 1, len(nums)
        lowest_length = float('inf')
        
        # Binary search
        while left <= right:
            mid = (left + right) // 2

            if isSumInLength(mid):
                lowest_length = min(lowest_length, mid)
                right = mid - 1
            else:
                left = mid + 1

        return 0 if lowest_length == float('inf') else lowest_length
                