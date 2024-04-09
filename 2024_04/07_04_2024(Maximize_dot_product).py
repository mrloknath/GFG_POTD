class Solution:
	def maxDotProduct(self, n, m, a, b):
		# code here
        def rec(i, j):
            if i == n and j != m:
                return float('-inf')
            if j == m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            tk = a[i] * b[j] + rec(i + 1, j + 1)
            ntk = rec(i + 1, j)
            dp[(i, j)] = max(tk, ntk)
            return dp[(i, j)]  
        
        dp = {}  
        return rec(0, 0)
