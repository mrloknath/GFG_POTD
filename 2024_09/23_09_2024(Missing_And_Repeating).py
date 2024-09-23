class Solution:
    def findTwoElement( self,arr): 
        n=len(arr)
        squared=0
        summation=0
        actual=(n*(n+1))//2
        squaredactual= (n*(n+1)*(2*n + 1))//6
        for i in range(n):
            summation+=arr[i]
            squared+=arr[i]**2
        diff=actual-summation
        missing=((squaredactual-squared)//diff + diff)//2
        repeated=missing-diff
        return repeated,missing
