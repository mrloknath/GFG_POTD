class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		d, i, j = 0, 0, 0
        while 0 <= i < n and 0 <= j < m:
            d = (d + matrix[i][j]) % 4
            if matrix[i][j] == 1:
                matrix[i][j] = 0

            if d == 0:
                j += 1
                if j == m:
                    j -= 1
                    break
            elif d == 1:
                i += 1
                if i == n:
                    i -= 1
                    break
            elif d == 2:
                j -= 1
                if j == -1:
                    j += 1
                    break
            elif d == 3:
                i -= 1
                if i == -1:
                    i += 1
                    break

        return [i, j]
