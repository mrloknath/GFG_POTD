class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [float('-inf')]*(n+1)
        dp[0] = 0
        for l in range(1, n+1):
            for s in [x, y, z]:
                if l >= s:
                    dp[l] = max(dp[l], dp[l-s]+1)
        return dp[-1] if dp[-1] != float('-inf') else 0
