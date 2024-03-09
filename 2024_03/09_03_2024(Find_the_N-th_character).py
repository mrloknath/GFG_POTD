#Author : Loknath Giri

class Solution:
    def nthCharacter(self, s, r, n):
        while r != 0:
            s = ''.join(['01' if char == '0' else '10' for char in s[:n + 1]])
            r -= 1
        return s[n]
