#Author: Loknath Giri

class Solution:
    def Distance(self,root,k,ans):
        if k==0:
            ans.append(root.data)
            return ans
        if root.left != None:
            self.Distance(root.left,k-1,ans)
        if root.right != None:
            self.Distance(root.right,k-1,ans)
        return
        
    def KDistance(self,root,k):
        '''
        :param root: root of given tree.
        :param k: distance k from root
        :return: list of all nodes that are at distance k from root.
        '''
        # code here
        ans=[]
        self.Distance(root,k,ans)
        return ans
    
