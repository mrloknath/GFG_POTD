class Solution:
    def firstElementKTime(self, n, k, a):
        mp = {}
        for i in range(n):
            if a[i] not in mp:
                mp[a[i]] = 1
            else:
                mp[a[i]] += 1
            if mp[a[i]] == k:
                return a[i]
        return -1
