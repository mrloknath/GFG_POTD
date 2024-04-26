class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        # code here 
        s = set()
        for i in range(n):
            s.add(arr1[i])
        for i in range(m):
            s.add(arr2[i])
        a=list(s)
        a.sort()
        return a
