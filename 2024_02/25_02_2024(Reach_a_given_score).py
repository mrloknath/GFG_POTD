class Solution:
    def count(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(3, n + 1):
            dp[i] += dp[i - 3]
        for i in range(5, n + 1):
            dp[i] += dp[i - 5]
        for i in range(10, n + 1):
            dp[i] += dp[i - 10]
        return dp[n]
