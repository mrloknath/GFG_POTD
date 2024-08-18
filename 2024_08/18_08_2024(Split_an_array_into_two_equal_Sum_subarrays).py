class Solution:
    def canSplit(self, nums):
        left, right = 0, len(nums) - 1
        current_sum = 0
        while left <= right:
            if current_sum <= 0:
                current_sum += nums[left]
                left += 1
            else:
                current_sum -= nums[right]
                right -= 1
        return current_sum == 0
