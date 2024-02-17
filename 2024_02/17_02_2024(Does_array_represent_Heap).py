from queue import Queue

class Solution:
    def isMaxHeap(self, arr, n):
        q = Queue()
        q.put(arr[0])
        i = 1
        while i < n:
            big = q.get()
            if arr[i] > big:
                return False
            q.put(arr[i])
            if i + 1 < n:
                if arr[i + 1] > big:
                    return False
                q.put(arr[i + 1])
                i += 1
            i += 1
        return True
