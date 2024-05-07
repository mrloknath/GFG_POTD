Author : Loknath Giri
Algorithm : BFS

def reverseLevelOrder(root):
    # code here
    q=[]
    q.append(root)
    ans=[]
    while len(q)>0:
        ans.append(q[0].data)
        node=q.pop(0)
        if node.right != None:
            q.append(node.right)
        if node.left != None:
            q.append(node.left)
    ans.reverse()
    return ans
