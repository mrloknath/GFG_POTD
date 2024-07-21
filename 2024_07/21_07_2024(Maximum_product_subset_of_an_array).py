class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        M = 10**9+7
        minv, maxv = arr[0], arr[0]
        
        for i in range(1, len(arr)):
            e = arr[i]
            minv, maxv = min(minv, minv*e, maxv*e, e), max(maxv, e*maxv, e*minv, e)
        return maxv%M
