class Solution:
    def AllPossibleStrings(self, s):
        ans = []
        cur = ""
        def sub(p):
            nonlocal cur
            if p == len(s):
                if len(cur):
                    ans.append(cur)
                return
            cur += s[p]
            sub(p + 1)
            cur = cur[:-1]
            sub(p + 1)
        sub(0)
        ans.sort()
        return ans
