class Solution:
    def minTime(self, root,target):
        # code here
        ans=[0]*1
        def fun(root):
            if root==None:
                return -1
            
            return max(1+fun(root.left),1+fun(root.right))
        
        def fun1(root):
            if root==None:
                return -1
            
            if root.data==target:
                x=fun(root)
                ans[0]=max(ans[0],x)
                return 1
            
            left=fun1(root.left)
            
            if left!=-1:
                x=fun(root.right)
                ans[0]=max(ans[0],x+left+1)
                return left+1
            
            right=fun1(root.right)
            
            if right!=-1:
                x=fun(root.left)
                ans[0]=max(ans[0],x+right+1)
                return right+1
            
            return -1
        
        fun1(root)
        return ans[0]
