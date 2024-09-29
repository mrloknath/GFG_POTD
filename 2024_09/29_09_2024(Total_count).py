class Solution:
    def totalCount(self, k, arr):
        c=0
        for i in arr:
            if i%k==0:
                c=c+(i//k)
            else:
                c=c+(i//k)+1
        return c
