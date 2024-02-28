class Solution:
    def DivisibleByEight(self, s: str) -> int:
        n = int(s[-3:]) if len(s) >= 3 else int(s)
        
        return -1 if n % 8 else 1
