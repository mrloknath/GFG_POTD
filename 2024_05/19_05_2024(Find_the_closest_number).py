from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        low = 0
        high = n - 1
        closest = arr[0]
        
        while low <= high:
            mid = (low + high) // 2
            
            if abs(arr[mid] - k) < abs(closest - k) or (abs(arr[mid] - k) == abs(closest - k) and arr[mid] > closest):
                closest = arr[mid]
            
            if arr[mid] < k:
                low = mid + 1
            elif arr[mid] > k:
                high = mid - 1
            else :
                return arr[mid]
        
        return closest
