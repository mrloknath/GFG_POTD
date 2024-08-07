
class Solution:
    def kthElement(self, k, arr1, arr2):
        def kth(arr1, arr2, i, j, m, n, k):
            if m > n:
                return kth(arr2, arr1, j, i, n, m, k)
                
            if m == 0:
                return arr2[j+k-1]
            if k == 1:
                return min(arr1[i], arr2[j])
                
            k1 = min(m, k//2)
            k2 = k-k1
            
            if arr1[i+k1-1] < arr2[j+k2-1]:
                return kth(arr1, arr2, i+k1, j, m-k1, n, k-k1)
            else:
                return kth(arr1, arr2, i, j+k2, m, n-k2, k-k2)
            
        return kth(arr1, arr2, 0, 0, len(arr1), len(arr2), k)
