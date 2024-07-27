class Solution:
    def countMin(self, str):
        # code
        m=len(str)
        from sys import setrecursionlimit
        setrecursionlimit(2*10**3)
        from functools import lru_cache
        @lru_cache(None)
        def lcs(i=0,j=m-1):
            nonlocal str
            if i>=j:
                return i==j
            if str[i]==str[j]:
                return lcs(i+1,j-1)+2
            mx=max(lcs(i+1,j),lcs(i,j-1))
            return mx
        return m-lcs()
