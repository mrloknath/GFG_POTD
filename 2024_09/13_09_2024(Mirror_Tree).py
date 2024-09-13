
class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        if not root:
            return None
        left = self.mirror(root.left)
        right = self.mirror(root.right)
        root.left, root.right = right, left
        return root
