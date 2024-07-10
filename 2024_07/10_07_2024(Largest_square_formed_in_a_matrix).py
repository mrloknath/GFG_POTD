from typing import List

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 or j==m-1:
                    ans=max(ans,mat[i][j])
                    continue
                if mat[i][j]==1:
                    mat[i][j]=min(mat[i+1][j],mat[i][j+1],mat[i+1][j+1])+1
                    ans=max(ans,mat[i][j])
        return ans 
