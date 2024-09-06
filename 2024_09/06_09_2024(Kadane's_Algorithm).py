class Solution:
    def maxSubArraySum(self,arr):
        running, s = 0, float('-inf')
        for e in arr:
            running += e
            s = max(s, running)
            running = max(running, 0)
        return s
