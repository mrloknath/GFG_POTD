class Solution:
    def countWays(self, n: int, s: str) -> int:
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        mod = 1003

        for i in range(n - 1, -1, -2):
            for j in range(i, n, 2):
                if i == j:
                    dp[i][j][1] = 1 if s[i] == 'T' else 0
                    dp[i][j][0] = 1 if s[i] == 'F' else 0
                else:
                    for k in range(i, j, 2):
                        f1, f0 = dp[i][k][1], dp[i][k][0]
                        s1, s0 = dp[k + 2][j][1], dp[k + 2][j][0]

                        if s[k + 1] == '&':
                            dp[i][j][1] += (f1 * s1) % mod
                            dp[i][j][0] += (f1 * s0 + f0 * s1 + f0 * s0) % mod
                        elif s[k + 1] == '|':
                            dp[i][j][1] += (f1 * s0 + f0 * s1 + f1 * s1) % mod
                            dp[i][j][0] += (f0 * s0) % mod
                        else:
                            dp[i][j][1] += (f1 * s0 + f0 * s1) % mod
                            dp[i][j][0] += (f1 * s1 + f0 * s0) % mod

        return dp[0][n - 1][1] % mod
