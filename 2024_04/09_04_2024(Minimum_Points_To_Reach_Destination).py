class Solution:
    def minPoints(self, m, n, points):
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - points[m - 1][n - 1])

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - points[i][n - 1])
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - points[m - 1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_points_on_exit - points[i][j])

        return dp[0][0]
