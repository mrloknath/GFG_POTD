class Solution:
    def swapElements(self, arr,n):
        if n == 1 or n == 2:
            return
        
        i, j = 0, 2
        while j < n:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
