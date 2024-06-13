class Solution:
    def padovanSequence(self, n):
        # code here 
        a, b, c, m = 1, 1, 1,10**9 + 7
        for i in range(3, n + 1):
            temp = (a + b) % m
            a = b
            b = c
            c = temp
        return c
