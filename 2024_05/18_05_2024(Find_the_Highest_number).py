from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
		lo = 0
        hi = len(a) - 1
        
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            ans = max(ans, a[mid])
            
            if mid == 0:
                lo = mid + 1
            elif mid == len(a) - 1:
                hi = mid - 1
            elif a[mid] < a[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return ans
