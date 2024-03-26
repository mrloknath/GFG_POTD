import itertools
class Solution:
    def isAdditiveSequence(self, n):
        l = len(n)
        for i, j in itertools.combinations(range(1, l), 2):
            a, b = n[:i], n[i:j]
            if b != str(int(b)):
                continue
            while j < l:
                c = str(int(a) + int(b))
                if not n.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == l:
                return 1
        return 0
