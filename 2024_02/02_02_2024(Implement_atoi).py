class Solution:
    def atoi(self, s: str) -> int:
        # Your code here
        ch = "qwertyuiopasdfghjklzxcvbnm"
        minus = "-"
        for i in range(len(s)):
            if s[i] in ch:
                return -1
            if s[i] in minus and i != 0:
                return -1
        ans = int(s)
        return ans
