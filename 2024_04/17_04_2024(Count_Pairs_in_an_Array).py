from typing import List

class Solution:
    def merge(self, arr: List[int], low: int, mid: int, high: int) -> int:
        temp = [0] * (high - low + 1)
        k = 0
        i = low
        j = mid + 1
        inv = 0
        
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                inv += mid - i + 1
                temp[k] = arr[j]
                k += 1
                j += 1
        
        while i <= mid:
            temp[k] = arr[i]
            k += 1
            i += 1
        
        while j <= high:
            temp[k] = arr[j]
            k += 1
            j += 1
        
        for x in range(low, high + 1):
            arr[x] = temp[x - low]
        
        return inv
    
    def mergeSort(self, arr: List[int], low: int, high: int) -> int:
        if low >= high:
            return 0
        inv = 0
        
        mid = (low + high) // 2
        
        inv += self.mergeSort(arr, low, mid)
        inv += self.mergeSort(arr, mid + 1, high)
        inv += self.merge(arr, low, mid, high)
        
        return inv
    
    def inversionCount(self, arr: List[int], N: int) -> int:
        return self.mergeSort(arr, 0, N - 1)
    
    def countPairs(self, arr: List[int], n: int) -> int:
        for i in range(n):
            arr[i] *= i
        return self.inversionCount(arr, n)
