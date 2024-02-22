class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def solve(self, i, j, n, m, s, t, dp):
        if j == m:
            return 1
        if i == n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = self.solve(i + 1, j, n, m, s, t, dp)
        if s[i] == t[j]:
            ans += self.solve(i + 1, j + 1, n, m, s, t, dp)
        dp[i][j] = ans % self.mod
        return dp[i][j]

    def sequenceCount(self, s, t):
        n = len(s)
        m = len(t)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return self.solve(0, 0, n, m, s, t, dp)
