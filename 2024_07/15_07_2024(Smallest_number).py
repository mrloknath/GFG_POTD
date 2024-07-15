class Solution:
    def smallestNumber(self, s, d):
        for i in range (pow(10,d-1),pow(10,d)+1):
            k=i
            sum=0
            while (k>0):
                r=k%10
                sum+=r
                k=k//10
            if sum==s:
                return i
        return -1        
