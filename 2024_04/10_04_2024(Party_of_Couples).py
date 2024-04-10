class Solution:
    def findSingle(self, n, arr):
        # code here
        result = 0
        
        # Perform XOR operation on all elements of the array
        for num in arr:
            result ^= num
        
        # The result will be the only single person in the party
        return result
