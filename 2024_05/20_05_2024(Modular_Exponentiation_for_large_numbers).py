class Solution:
	def PowMod(self, x, n, m):
		# Code here
		ans = 1
        while n > 0:
            if n&1 != 0:
                ans = (ans*x)%m
            x = x*x%m
            n >>= 1
        return ans
