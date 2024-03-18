class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        if not root:
            return []
        
        q = deque([root])
        ans = []
        
        while q:
            cur = q.popleft()
            ans.append(cur.data)
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return ans
