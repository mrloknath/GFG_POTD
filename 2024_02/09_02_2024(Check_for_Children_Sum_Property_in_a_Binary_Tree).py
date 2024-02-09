class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def rec(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
            
        l = self.rec(root.left)
        r = self.rec(root.right)
        
        if l + r == root.data:
            return root.data
        return -1000000
    
    def isSumProperty(self, root):
        ans = self.rec(root)
        if ans < 0:
            return 0
        return 1
