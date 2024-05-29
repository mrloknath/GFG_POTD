class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        # code here
        # Initialize a DP array
        dp = [False] * (n + 1)
        dp[0] = False  # No coins left is a losing state

        for i in range(1, n + 1):
            # Check if any of the moves leave the opponent in a losing state
            if i - 1 >= 0 and not dp[i - 1]:
                dp[i] = True
            elif i - x >= 0 and not dp[i - x]:
                dp[i] = True
            elif i - y >= 0 and not dp[i - y]:
                dp[i] = True
            else:
                dp[i] = False

        return 1 if dp[n] else 0
