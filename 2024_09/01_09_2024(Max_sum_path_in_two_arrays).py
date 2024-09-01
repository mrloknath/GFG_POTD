class Solution:
    def maxPathSum(self, arr1, arr2):
        arr1, arr2 = [0] + arr1, [0] + arr2
        s1, s2 = 0, 0
        while arr1 or arr2:
            if arr1[-1] == arr2[-1]:
                s1 = s2 = max(s1, s2) + arr1.pop()
                arr2.pop()
            elif arr1[-1] > arr2[-1]:
                s1 += arr1.pop()
            else:
                s2 += arr2.pop()
        return max(s1, s2)
