class Solution:
	def editDistance(self, str1, str3):
        m, n = len(str1), len(str3)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i+1][0] = i+1
        for i in range(n):
            dp[0][i+1] = i+1
        for i in range(m):
            for j in range(n):
                if str1[i] == str3[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
        return dp[-1][-1]
