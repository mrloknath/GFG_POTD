class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        MOD = int(1e9 + 7)
        
        if n == 1:
            return 0
        
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        
        a[1] = 1
        b[1] = 1
        
        for i in range(2, n + 1):
            a[i] = (a[i - 1] + b[i - 1]) % MOD
            b[i] = a[i - 1]
        
        no_consec_ones = (a[n] + b[n]) % MOD
        total_strings = pow(2, n, MOD)
        
        result = (total_strings - no_consec_ones + MOD) % MOD
        return result
