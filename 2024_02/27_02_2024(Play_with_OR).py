class Solution:
    def game_with_number (self, arr,  n) : 
        n = len(arr)
        for i in range(n):
            if i == n-1:
                continue
            else:
                arr[i] = arr[i] | arr[i+1]
        return arr
