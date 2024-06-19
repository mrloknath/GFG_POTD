class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        for a in range(1, 2*r + 1):
            for b in range(1, 2*r + 1):
                if a*a + b*b <= 4*r*r:
                    count += 1
        return count
