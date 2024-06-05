class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        suma = sum(a)
        sumb = sum(b)
        if (suma - sumb) % 2 != 0:
            return -1
        target = (suma - sumb) // 2
        a.sort()
        b.sort()
        i, j = 0, 0
        while i < n and j < m:
            diff = a[i] - b[j]
            if diff == target:
                return 1
            elif diff < target:
                i += 1
            else:
                j += 1  
        return -1
