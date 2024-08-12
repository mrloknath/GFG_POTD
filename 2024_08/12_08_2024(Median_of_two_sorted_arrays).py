class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        ans=arr1+arr2 #merges two arrays together
        ans.sort()
        n=len(ans)
        return ans[n//2-1]+ans[n//2]
