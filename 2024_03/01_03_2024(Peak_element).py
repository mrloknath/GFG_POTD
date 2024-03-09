#Author : Loknath Giri

class Solution:
    def findMaxPosition(self, arr):
        max_val = arr[0]
        p = 0
        for i in range(1, len(arr)):
            if max_val < arr[i]:
                max_val = arr[i]
                p = i
        return p

    def peakElement(self, arr,n):
        if n == 1:
            return 0
        elif n == 2:
            return self.findMaxPosition(arr)
        else:
            return self.findMaxPosition(arr)
