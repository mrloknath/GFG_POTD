class Solution:
    def reversedBits(self, x):
        # code here 
        arr=bin(x)[2:]
        n = len(arr)
        rem= 32- n
        for i in range(rem):
            arr='0'+ arr
        arr= arr[::-1]
        
        return int(arr, 2)
