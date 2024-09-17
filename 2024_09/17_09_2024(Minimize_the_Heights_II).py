class Solution:
    def getMinDiff(self, arr, k):
        n=len(arr)
        arr.sort()
        res = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] >= k:
                max_val = max(arr[i-1] + k, arr[-1] - k)
                min_val = min(arr[0] + k, arr[i] - k)
                res = min(res, max_val - min_val)
        return res
