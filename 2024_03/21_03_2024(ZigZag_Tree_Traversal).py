
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        if not root:
            return []

        result = []
        current_level = []
        next_level = []
        left_to_right = True
        current_level.append(root)

        while current_level:
            node = current_level.pop()
            result.append(node.data)

            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

            if not current_level:
                current_level, next_level = next_level, current_level
                left_to_right = not left_to_right

        return result
        
