class Solution:
    def verticalSum(self, root):
        """
        :param root: root of the given tree.
        :return: A list of sums of nodes in each vertical line.
        """
        if not root:
            return []

        column_sum = {}
        min_column = max_column = 0
        queue = [(root, 0)]  # (node, column)

        while queue:
            node, column = queue.pop(0)
            if column not in column_sum:
                column_sum[column] = 0
            column_sum[column] += node.data

            if column < min_column:
                min_column = column
            if column > max_column:
                max_column = column

            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))

        return [column_sum[i] for i in range(min_column, max_column + 1)]
