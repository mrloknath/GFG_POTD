class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        
        if not root:
            return -1
            
        while root.left is not None:
               root=root.left
        return (root.data)
