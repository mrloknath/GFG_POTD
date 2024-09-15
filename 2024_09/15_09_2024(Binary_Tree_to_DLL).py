class Solution:
    def bToDLL(self, root):
        
        def dfs(node):
            first = last = node
            if node.left:
                first, node.left = dfs(node.left)
                node.left.right = node
            if node.right:
                node.right, last = dfs(node.right)
                node.right.left = node
            return first, last
        
        return dfs(root)[0]
