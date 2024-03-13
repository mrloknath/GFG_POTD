class Solution:
    def matrixDiagonally(self, mat):
        n = len(mat)
        result = []

        for d in range(n * 2 - 1):
            if d % 2 == 0:
                row, col = min(d, n - 1), max(0, d - n + 1)
                while row >= 0 and col < n:
                    result.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                row, col = max(0, d - n + 1), min(d, n - 1)
                while row < n and col >= 0:
                    result.append(mat[row][col])
                    row += 1
                    col -= 1

        return result
