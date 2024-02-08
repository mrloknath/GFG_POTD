class Solution:
    def check(self, root):
        s = set()
        def dfs(n, d=0):
            if not n:
                return
            if not n.left and not n.right:
                s.add(d)
                return
            dfs(n.left, d+1)
            dfs(n.right, d+1)
        dfs(root)
        return len(s) == 1
