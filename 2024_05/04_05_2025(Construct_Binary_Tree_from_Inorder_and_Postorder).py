class Solution:
    def buildTree(self,In, post, n):
    # your code here
        def helper(In,post,n):
            if not In or not post:
                return None
                
            root_val = post.pop()
            root = Node(root_val)
            
            root_index = In.index(root_val)
            
            root.right = helper(In[root_index+1:],post,n)
            root.left = helper(In[:root_index],post,n)
            
            return root
        return helper(In,post,n)
        
