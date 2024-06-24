class Solution:
    def sumMatrix(self, n, q):
        # code here 
        diff = abs((n + 1) - q)
        return max(n - diff, 0)
