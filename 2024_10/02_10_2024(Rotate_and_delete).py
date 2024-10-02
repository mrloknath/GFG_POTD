class Solution:
    def rotateDelete(self,  arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
        if n == 2:
            return arr[1]
        index = 0
        if n%2 == 0:
            if n%4 == 0:
                index = n//4
            else:
                index = (n//4) + 1
        else:
            if n%4 == 1:
                index = (n-1)//4 + 1
            else:
                index = (n+1)//4 + 1
        return arr[index]
