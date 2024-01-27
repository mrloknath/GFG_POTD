class Solution:
    
    def matrixChainOrder(self, p, n):
        v = [[("", -1) for _ in range(n)] for _ in range(n)]

        operations = self.solve(p, n, 1, n - 1, v)

        return operations[0]

    def solve(self, p, n, i, j, v):
        if i == j:
            s = chr(ord('A') + i - 1)
            return (s, 0)

        if v[i][j][1] != -1:
            return v[i][j]

        mini = float('inf')
        sr = ""
        for k in range(i, j):
            left = self.solve(p, n, i, k, v)
            right = self.solve(p, n, k + 1, j, v)

            steps = left[1] + right[1] + p[i - 1] * p[k] * p[j]

            if steps < mini:
                sr = '(' + left[0] + right[0] + ')'
                mini = steps

        v[i][j] = (sr, mini)
        return v[i][j]

