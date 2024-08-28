from collections import Counter
class Solution:
    def sortByFreq(self,arr):
        f = Counter(arr)
        return sorted(arr, key=lambda x: (-f[x], x))
