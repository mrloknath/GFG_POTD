class Solution:
    def pairAndSum(self, n, arr):
        #code here
        sum=0
        for i in range(32):
            count=0
            for j in arr:
                if j&(1<<i):
                    count+=1
            sum+=count*(count-1)//2*(1<<i)
        return sum
