
class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        if(n<3 or m<3):
            return -1
        ans=-1
        sum=0
        for i in range(0,n-2):
            for j in range(0,m-2):
                sum=mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]
                ans=max(ans,sum)
        return ans
