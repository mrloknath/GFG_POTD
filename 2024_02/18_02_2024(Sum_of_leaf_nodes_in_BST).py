class Solution:
    def solve(self, root, sum):
        if root is None:
            return
        if root.left is None and root.right is None:
            sum[0] += root.data
            return
        self.solve(root.left, sum)
        self.solve(root.right, sum)

    def sumOfLeafNodes(self, root):
        sum = [0]
        self.solve(root, sum)
        return sum[0]
