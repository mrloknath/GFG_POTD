class Solution:
    def countPairs(self, mat1, mat2, n, x):
        ans = 0
        r1, c1 = 0, 0
        r2, c2 = n-1, n-1
        while r1 < n and r2 >= 0:
            sum = mat1[r1][c1] + mat2[r2][c2]
            if sum == x:
                ans += 1
                c1 += 1
                c2 -= 1
            elif sum < x:
                c1 += 1
            else:
                c2 -= 1
            if c1 == n:
                r1 += 1
                c1 = 0
            if c2 < 0:
                r2 -= 1
                c2 = n-1
        return ans
