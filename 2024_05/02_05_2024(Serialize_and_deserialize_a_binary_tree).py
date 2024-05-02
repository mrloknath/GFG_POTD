
class Solution:
    def solve(self, A, ind):
        if A[ind] == -1:
            ind += 1
            return None, ind
        root = Node(A[ind])
        ind += 1
        root.left, ind = self.solve(A, ind)
        root.right, ind = self.solve(A, ind)
        return root, ind

    def pre(self, root, ans):
        if not root:
            ans.append(-1)
            return
        ans.append(root.data)
        self.pre(root.left, ans)
        self.pre(root.right, ans)
        
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        ans = []
        self.pre(root, ans)
        return ans
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
        ind = 0
        return self.solve(A, ind)[0]
    
