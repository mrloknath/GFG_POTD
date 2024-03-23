#Author : Loknath Giri

class Solution:
    def series(self, n):
        fs=[0,1]
        if(n==0):
            return [0]
        elif(n==1):
            return fs
        else :
            for i in range(2,n+1):
                fs.append((fs[i-1]+fs[i-2])%(10**9+7))
            return fs
