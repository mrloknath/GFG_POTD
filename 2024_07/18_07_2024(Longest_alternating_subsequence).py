class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        inc, dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = dec+1
            elif nums[i] < nums[i-1]:
                dec = inc+1
        return max(dec, inc)
