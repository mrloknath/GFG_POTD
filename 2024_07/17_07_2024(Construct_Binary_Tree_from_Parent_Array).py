class Solution:
    # Function to construct a binary tree from a parent array.
    def createTree(self, parent):
        temp = {}
        for key, parent_index in enumerate(parent):
            node = temp[parent_index] = temp.get(parent_index, Node(parent_index))
            if not node.left:
                node.left = temp[key] = temp.get(key, Node(key))
            else:
                node.right = temp[key] = temp.get(key, Node(key))
        return temp[-1].left
