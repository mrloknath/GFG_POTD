from collections import deque

class Solution:
    def bottomView(self, root):
        # code here
        if root==None:
            return []
        ans=[]
        map={}
        q=deque()
        q.append((root, 0))
        while q:
            x=q.popleft()
            line=x[1]
            node=x[0]
            map[line]=node.data
            if node.left:
                q.append((node.left, line-1))
            if node.right:
                q.append((node.right, line+1))
        for key in sorted(map.keys()):
            ans.append(map[key])
        return ans
