class Solution:
    def inorder(self,root):
        l=[]
        def helper(node):
            if node is None:
                return None
            helper(node.left)
            l.append(node.data)
            helper(node.right)
            return l
        return helper(root)
    def merge(self, root1, root2):
        final=self.inorder(root1)+self.inorder(root2)
        final.sort()
        return final

