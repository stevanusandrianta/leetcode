class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        left, right = 0, 0
        n = len(nums)
        current_sum = 0

        result = float('inf')

        while left < n and right < n:
            while current_sum < target and right < n:
                current_sum += nums[right]
                right += 1
            
            while current_sum >= target and left < n:
                result = min(result, right-left)
                current_sum -= nums[left]
                left += 1
            
        return result
