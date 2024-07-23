class Solution:
    def merge(self, root1, root2):
        def dfs(node, arr):
            if not node:
                return
            dfs(node.left, arr)
            arr.append(node.data)
            dfs(node.right, arr)
        bst1, bst2 = [], []
        dfs(root1, bst1)
        dfs(root2, bst2)
        return sorted(bst1 + bst2)
