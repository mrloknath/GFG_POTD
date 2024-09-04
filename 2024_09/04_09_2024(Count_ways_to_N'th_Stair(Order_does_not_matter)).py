class Solution:
	def nthStair(self,n):
		# Code here
        dp = [[0, 0] for _ in range(n+1)]
        dp[0] = [1, 0]
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0]
            if i > 1:
                dp[i][1] = sum(dp[i-2])
        return sum(dp[-1])
