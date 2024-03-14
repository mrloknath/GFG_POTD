class Solution:
    def largestSubsquare(self, n, a):
        ver = [[0] * n for _ in range(n)]
        hor = [[0] * n for _ in range(n)]
        side = 0
        
        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    ver[i][j] = 1 if i == 0 else ver[i - 1][j] + 1
                    hor[i][j] = 1 if j == 0 else hor[i][j - 1] + 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                val = min(ver[i][j], hor[i][j])
                while val > side:
                    if ver[i][j - val + 1] >= val and hor[i - val + 1][j] >= val:
                        side = val
                    val -= 1
        
        return side
