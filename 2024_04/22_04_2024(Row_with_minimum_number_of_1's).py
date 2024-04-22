class Solution:
    def minRow(self,n,m,a):
        #code here
        ans = {}
        for i in range(n):
            ans[i+1] = a[i].count(1)
        return sorted(ans.items(), key = lambda t:t[1])[0][0]
