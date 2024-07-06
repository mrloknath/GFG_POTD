class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    def populateNext(self, root):
        def inorder(node):
            nonlocal prev
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                prev.next = node
            prev = node
            inorder(node.right)
        prev = None
        inorder(root)
