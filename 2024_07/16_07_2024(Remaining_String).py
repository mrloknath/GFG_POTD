class Solution:
    def printString(self, s, ch, count):
        # code here 
        for i, c in enumerate(s):
            if c == ch: count -= 1
            if count == 0: return s[i+1:]
        return ""
