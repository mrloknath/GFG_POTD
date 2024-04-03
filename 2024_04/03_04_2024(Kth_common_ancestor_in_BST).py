class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        # Code here
        # Make sure x < y
        if x > y:
            x, y = y, x
        ancestors, node = [root.data], root
        while not (x <= node.data <= y):
            if x < node.data:
                node = node.left
            else:
                node = node.right
            ancestors.append(node.data)
        return ancestors[-k] if len(ancestors) >= k else -1
