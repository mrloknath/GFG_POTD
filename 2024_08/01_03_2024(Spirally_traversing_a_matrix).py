
class Solution:
    def spirallyTraverse(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        k = 2 * min(m, n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, -1
        res = []
        for d in range(k):
            for i in range(n):
                x += dx[d % 4]
                y += dy[d % 4]
                res.append(matrix[x][y])
            m, n = n, m - 1
        return res
