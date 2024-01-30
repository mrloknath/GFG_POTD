class Solution:
    def __init__(self):
        self.dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

    def solve(self, A, B, C, i, j, k):
        if i < 0 or j < 0 or k < 0:
            return 0
        if self.dp[i][j][k] is not None:
            return self.dp[i][j][k]
        if A[i] == B[j] == C[k]:
            self.dp[i][j][k] = 1 + self.solve(A, B, C, i - 1, j - 1, k - 1)
        else:
            self.dp[i][j][k] = max(
                self.solve(A, B, C, i - 1, j, k),
                max(self.solve(A, B, C, i, j - 1, k), self.solve(A, B, C, i, j, k - 1)),
            )
        return self.dp[i][j][k]

    def LCSof3(self, A, B, C, n1, n2, n3):
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                for k in range(n3 + 1):
                    self.dp[i][j][k] = None

        return self.solve(A, B, C, n1 - 1, n2 - 1, n3 - 1)
