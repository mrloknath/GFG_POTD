class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        import sys
        sys.setrecursionlimit(10**6)
        from functools import lru_cache
        
        @lru_cache(None)
        def match(i, j):
            if i < 0:
                return 1
            if j < 0:
                return 0
            r = match(i, j-1)

            if s2[i] == s1[j]:
                r += match(i-1, j-1)
            return r%(10**9+7)
        return match(len(s2)-1, len(s1)-1)
