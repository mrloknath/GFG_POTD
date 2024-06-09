from typing import List
class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        for i in range(len(arr)-1):
            if (i&1) and arr[i]<arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            elif not (i&1) and arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
