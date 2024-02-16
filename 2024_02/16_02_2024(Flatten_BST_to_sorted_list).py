class Solution:
    def flattenBST(self, root):
        # code here
        import sys
        
        sys.setrecursionlimit(10 ** 6)
        head = Node(0)
        
        def dfs(node, head):
            if not node:
                return head
            
            left, right = node.left, node.right
            node.left = node.right = None
            dfs(left, head).right = node
            return dfs(right, node)
        
        dfs(root, head)
        return head.right
