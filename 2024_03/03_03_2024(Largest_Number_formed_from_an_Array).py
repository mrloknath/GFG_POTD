class Solution:

    def printLargest(self, n, arr):
        def compare(a, b):
            order1 = a + b
            order2 = b + a
            if order1 > order2:
                return -1  
            elif order1 < order2:
                return 1   
            else:
                return 0   
        arr.sort(key=functools.cmp_to_key(compare))
        return ''.join(arr)
