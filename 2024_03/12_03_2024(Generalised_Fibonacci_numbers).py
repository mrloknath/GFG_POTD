class Solution:
    def matmul(self, a, b, m):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % m
        return result

    def genFibNum(self, a, b, c, n, m):
        if n <= 2:
            return 1

        res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        gen_fib_matrix = [[a, b, c], [1, 0, 0], [0, 0, 1]]

        n -= 2
        while n:
            if n & 1:
                res = self.matmul(res, gen_fib_matrix, m)
            gen_fib_matrix = self.matmul(gen_fib_matrix, gen_fib_matrix, m)
            n >>= 1

        return sum(res[0]) % m
