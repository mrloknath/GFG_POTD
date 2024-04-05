class Solution:
    def min_operations(self,nums):
        n = len(nums)
        LIS = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and (i - j) <= (nums[i] - nums[j]):
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return n - max(LIS)
