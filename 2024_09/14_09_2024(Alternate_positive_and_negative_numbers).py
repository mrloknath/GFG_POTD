class Solution:
    def rearrange(self,arr):
        # code here
        i, j, n = 0, 0, len(arr)
        ret = []
        
        while i < n or j < n:
            while i < n and arr[i] < 0:
                i += 1
            while j < n and arr[j] >= 0:
                j += 1
            if i < n:
                ret.append(arr[i])
                i += 1
            if j < n:
                ret.append(arr[j])
                j += 1
        arr[:] = ret
