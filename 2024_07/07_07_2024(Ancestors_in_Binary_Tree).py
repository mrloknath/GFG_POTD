class Solution:
    def __init__(self):
        self.stack = []
    def dfs(self,root,target):
        if not root:
            return False
        if root.data==target:
            return True
        if self.dfs(root.left,target):
            self.stack.append(root.data)
            return True
        if self.dfs(root.right,target):
            self.stack.append(root.data)
            return True
        return False

    def Ancestors(self, root, target):
        self.stack = []
        self.dfs(root,target)
        return self.stack
