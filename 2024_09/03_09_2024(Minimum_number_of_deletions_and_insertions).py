class Solution:
    def minOperations(self, s1, s2):
        m=len(s1)
        n=len(s2)
        from functools import lru_cache
        @lru_cache(None)
        def dp(a=m-1,b=n-1):
            nonlocal s1,s2
            if a<0 or b<0:
                return b+1 if a<0 else a+1
            mn=min(dp(a-1,b),dp(a,b-1))+1
            if s1[a]==s2[b]:
                mn=min(mn,dp(a-1,b-1))
            return mn
        return dp()
