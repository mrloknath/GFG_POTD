
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        pre=arr[0]
        for word in arr[1:]:
            i=0
            for c in word:
                if i>=len(pre) or c!= pre[i]:
                    break
                i+=1
            pre=pre[:i]
        return pre if len(pre)>0 else -1
