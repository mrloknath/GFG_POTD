class Solution:
    def lcs(self, x: str, y: str) -> int:
        n, m = len(x), len(y)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]
    
    def findMinCost(self, x: str, y: str, costX: int, costY: int) -> int:
        length = self.lcs(x, y)
        return costX * (len(x) - length) + costY * (len(y) - length)
