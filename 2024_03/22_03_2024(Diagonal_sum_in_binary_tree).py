class Solution:
    #Complete the function below
    def diagonalSum(self, root):
        #:param root: root of the given tree.
        
        from collections import defaultdict
        diagonal_sum = defaultdict(int)
        
        def dfs(node, row, col):
            if not node:
                return
            diagonal_sum[row - col] += node.data
            if node.left:
                dfs(node.left, row + 1, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        return [value for _, value in sorted(diagonal_sum.items())]
