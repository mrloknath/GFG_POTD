from bisect import bisect_right
class Solution:
    def countElements(self, a, b, n, query, q):
        b.sort()
        return [bisect_right(b, a[q]) for q in query]
