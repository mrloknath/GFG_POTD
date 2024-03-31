class Solution:
    def _init_(self):
        self.ans = float('-inf')
    
    def solve(self, root, n):
        if root is None:
            return
        if root.key <= n:
            self.ans = max(self.ans, root.key)
            self.solve(root.right, n)
        else:
            self.solve(root.left, n)
