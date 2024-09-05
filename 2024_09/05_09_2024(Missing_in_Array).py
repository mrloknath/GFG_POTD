class Solution:
    def missingNumber(self, n, arr):
        import operator
        from functools import reduce
        return reduce(operator.xor, (i ^ a for i, a in enumerate(arr, 1)), n)
