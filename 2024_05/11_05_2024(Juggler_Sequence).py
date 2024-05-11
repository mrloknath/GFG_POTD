#Author : Loknath Giri

import math

class Solution:
    def jugglerSequence(self, n):
        # code here
        ans=[n]
        while n>=2:
            if n%2==0:
                n=int(math.sqrt(n))
            else:
                n=int(math.sqrt(n*n*n))
            ans.append(n)
        return ans
