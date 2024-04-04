Author : Loknath Giri

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        # code here
        previous, current, ans = 0, 0, 0
        mod = 10**9 + 7
        for i in range(len(s)):
            current = (int(s[i]) * (i + 1)) + (previous * 10)
            current %= mod
            ans += current
            ans %= mod
            previous = current
        return ans
