#User function Template for python3
class Solution:
    def swapNibbles(self, n: int) -> int:
        #code here
        rn = n & 0b11110000
        ln = n & 0b00001111
        
        rn = rn >> 4
        ln = ln << 4
        
        return rn | ln
