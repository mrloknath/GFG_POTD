class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def lca(self, root, a, b):
        if root is None:
            return None
        if root.data == a or root.data == b:
            return root
        left = self.lca(root.left, a, b)
        right = self.lca(root.right, a, b)
        if right is None:
            return left
        elif left is None:
            return right
        else:
            return root
    
    def solve(self, root, val):
        if root is None:
            return 0
        if root.data == val:
            return 1
        a = self.solve(root.left, val)
        b = self.solve(root.right, val)
        if a == 0 and b == 0:
            return 0
        else:
            return a + b + 1
    
    def findDist(self, root, a, b):
        LCA = self.lca(root, a, b)
        x = self.solve(LCA, a)
        y = self.solve(LCA, b)
        return x + y - 2
