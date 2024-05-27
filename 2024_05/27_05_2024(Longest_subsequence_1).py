from typing import List

class Solution:
    def longestSubseq(self, N, A):
        dp, max1 = [1] * N, float("-inf")

        for i in range(1, N):
            for j in range(i):
                if abs(A[i] - A[j]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max1 = max(max1, dp[i])
        return max1
