class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return target == root.data
        new_target = target - root.data
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)
