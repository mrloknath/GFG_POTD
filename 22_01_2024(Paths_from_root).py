class Solution:
    def printPathsUtil(self, curr_node, target_sum, sum_so_far, path, ans):
        if not curr_node:
            return
        sum_so_far += curr_node.data
        path.append(curr_node.data)
        if sum_so_far == target_sum:
            ans.append(path[:])
        if curr_node.left:
            self.printPathsUtil(curr_node.left, target_sum, sum_so_far, path, ans)
        if curr_node.right:
            self.printPathsUtil(curr_node.right, target_sum, sum_so_far, path, ans)
        path.pop()
    def printPaths(self, root, sum):
        path = []
        ans = []
        self.printPathsUtil(root, sum, 0, path, ans)
        return ans
