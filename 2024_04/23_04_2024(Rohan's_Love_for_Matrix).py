Author:Loknath Giri

class Solution:
    def firstElement (self, n):
        # code here 
        if n == 0 or n == 1:
            return 1
        a, b = 1, 1
        mod = 1000000007
        for i in range(n - 2):
            c = (a + b) % mod
            a = b % mod
            b = c % mod
        return c % mod

