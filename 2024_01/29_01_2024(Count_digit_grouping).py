class Solution:
    def solve(self, ind, sum, str, n, dp):
        if ind == n:
            return 1
        if dp[ind][sum] != -1:
            return dp[ind][sum]
        ans, curr = 0, 0
        for i in range(ind, n):
            curr += int(str[i])
            if curr >= sum:
                ans += self.solve(i + 1, curr, str, n, dp)
        dp[ind][sum] = ans
        return ans

    def TotalCount(self, str):
        n = len(str)
        dp = [[-1 for _ in range(9 * n + 1)] for _ in range(n + 1)]
        return self.solve(0, 0, str, n, dp)
