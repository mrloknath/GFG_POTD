class Solution:
    def minimizeCost(self, k, arr):
        n=len(arr)
        dp=[float ('inf')]*n
        dp[0]=0
        for i in range(1,n):
            for j in range(max(0,i-k),i):
                dp[i]=min(dp[i],dp[j]+abs(arr[i]-arr[j]))
        return dp[n-1]
