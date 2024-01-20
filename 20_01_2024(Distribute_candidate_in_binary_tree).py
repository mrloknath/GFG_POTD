
class Solution:
    def solve(self, root, moves):
        if not root:
            return 0
        left_ans = self.solve(root.left, moves)
        right_ans = self.solve(root.right, moves)
        moves[0] += abs(left_ans) + abs(right_ans)
        return root.data - 1 + left_ans + right_ans

    def distributeCandy(self, root):
        moves = [0]
        self.solve(root, moves)
        return moves[0]
