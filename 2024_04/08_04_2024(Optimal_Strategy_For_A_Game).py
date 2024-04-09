class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        map = {}
        def solve(i, j):
            if i > j or i >= n or j < 0:
                return 0
            k = (i, j)
            if k in map:
                return map[k]
            option1 = arr[i] + min(solve(i+2, j),solve(i+1, j-1))
            option2 = arr[j] + min(solve(i+1, j-1),solve(i, j-2))
            map[k] = max(option1, option2)
            return map[k]
        return solve(0, n-1)
