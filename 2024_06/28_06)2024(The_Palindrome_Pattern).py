class Solution:
    def pattern (self, arr):
    # code here
        n = len(arr)
        for i in range(n):
            if arr[i] == arr[i][::-1]:
                return "{} R".format(i)
        for i in range(n):
            column = [arr[j][i] for j in range(n)]
            if column == column[::-1]:
                return "{} C".format(i)
        return "-1"
        
