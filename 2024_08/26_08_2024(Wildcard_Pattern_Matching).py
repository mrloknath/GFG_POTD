class Solution:
    def wildCard(self, pattern, string):
        from functools import lru_cache
        n, m = len(pattern), len(string)
        
        @lru_cache(maxsize=None)
        def dfs(i=0, j=0):
            if i == n:
                return j == m
            elif j == m:
                return pattern[i] == "*" and dfs(i + 1, m)
            elif pattern[i] == "?" or pattern[i] == string[j]:
                return dfs(i + 1, j + 1)
            elif pattern[i] == "*":
                return dfs(i + 1, j) or dfs(i, j + 1)
            else:
                return False
        
        return int(dfs())
