class Solution:
    def find3Numbers(self, arr):
        ret=[]
        m=len(arr)
        def dfs(ix=m-1,prv=float('inf')):
            nonlocal arr,ret
            if len(ret)==3:
                return True
            if ix<0:
                return False
            if arr[ix]<prv:
                ret.append(arr[ix])
                if dfs(ix-1,arr[ix]):
                    return True
                ret.pop()
            if dfs(ix-1,prv):
                return True
            return False
        dfs()
        return ret[::-1]
