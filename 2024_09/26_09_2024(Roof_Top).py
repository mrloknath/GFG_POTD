class Solution:
    def maxStep(self, arr):
        ct = mx = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]: ct += 1
            else: ct = 0
            mx = max(mx,ct)
        return mx  
