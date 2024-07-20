class Solution:
    def RemoveHalfNodes(self, root):
        #code here
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left = self.RemoveHalfNodes(root.left)
        root.right = self.RemoveHalfNodes(root.right)
        if root.left and not root.right:
            return root.left
        if not root.left and root.right:
            return root.right
        return root
