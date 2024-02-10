class Solution:
    
    def numberOfPath(self, n, k, arr):
        dr = [1, 0]
        dc = [0, 1]
        
        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        
        dp = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        
        def helper(r, c, summ):
            if r == n - 1 and c == n - 1:
                return 1 if summ == arr[r][c] else 0
            
            if dp[r][c][summ] != -1:
                return dp[r][c][summ]
            
            dp[r][c][summ] = 0
                
            if arr[r][c] <= summ:
                for direction in range(2):
                    nr = r + dr[direction]
                    nc = c + dc[direction]
                    
                    if valid(nr, nc):
                        dp[r][c][summ] += helper(nr, nc, summ - arr[r][c])
            
            return dp[r][c][summ]
        
        return helper(0, 0, k)
