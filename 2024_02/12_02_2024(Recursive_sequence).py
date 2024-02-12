class Solution:
    def sequence(self, n):
        mod = 10**9 + 7 

        p = 1  
        ans = 0  

        for i in range(1, n + 1): 
            val = 1 

            for j in range(i): 
                val = (val * p) % mod 
                p += 1  
            ans = (ans + val) % mod  

        return ans
