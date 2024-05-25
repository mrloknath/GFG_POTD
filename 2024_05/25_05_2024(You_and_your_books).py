class Solution:
     def max_Books(self, n, k, arr):
        from itertools import groupby
        gs = groupby(arr, key=lambda x: x <= k)
        sums = [sum(e) for f, e in gs if f]
        return max(sums) if sums else 0
