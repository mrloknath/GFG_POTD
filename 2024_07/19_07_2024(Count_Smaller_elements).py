import bisect
class Solution:
    def constructLowerArray(self,arr):
        ans=[0]
        right=[arr[-1]]
        for i in range(len(arr)-2,-1,-1):
            #count of element smaller than arr[i] in right
            count=bisect.bisect_left(right,arr[i])
            bisect.insort(right,arr[i])
            ans.append(count)
        return ans[::-1]
