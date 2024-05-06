Author : Loknath Giri

def noSibling(root):
    # code here
    ans=[]
    def check(root, ans):
        if root==None:
            return ans
        if root.right ==None and root.left !=None:
            ans.append(root.left.data)
        elif root.right !=None and root.left ==None:
            ans.append(root.right.data)
        ans = check(root.left, ans)
        ans = check(root.right, ans)
        return ans
    ans = check(root,ans)
    if not ans:
        return [-1]
    ans.sort()
    return ans
