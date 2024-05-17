from typing import List
class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort()
        front=back=0
        while front<n:
            if arr[front]-arr[back]==x:
                return 1
            elif arr[front]-arr[back]>x:
                back+=1
            elif arr[front]-arr[back]<x:
                front+=1
        return -1
