class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #code here
        def dfs(node):
            if not node:
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left[1] > right[1]:
                ans = left
            elif right[1] > left[1]:
                ans = right
            else:
                ans = (max(left[0], right[0]), left[1])
            
            ans = (ans[0] + node.data, ans[1] + 1)
            
            return ans
        
        return dfs(root)[0]
