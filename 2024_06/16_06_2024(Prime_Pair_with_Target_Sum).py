from typing import List

class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        if n < 3:
            return [-1, -1]

        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        # Find the pair of primes
        for a in range(2, n):
            if is_prime[a] and is_prime[n - a]:
                return [a, n - a]
        
        return [-1, -1]
        
