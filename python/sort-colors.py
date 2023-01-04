class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        left, right, n = 0, 0, len(nums)
        unique_values = [0,1,2]
        
        for value in unique_values:
            right = left
            while right < n:
                if nums[right] == value:
                    if left == right:
                        left += 1
                    else:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                right += 1