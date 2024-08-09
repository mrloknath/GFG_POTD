class Solution:
    def Maximize(self, a): 
        ans=0
        a.sort()
        for i in range(len(a)):
            ans=ans+a[i]*i
        return (ans%(10**9+7))
      
