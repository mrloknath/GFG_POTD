def LeftView(root):
    # code here
    m = {}
    def walk(n, level):
        nonlocal m
        if not n:
            return
        m[level] = n.data
        walk(n.right, level+1)
        walk(n.left, level+1)
    walk(root, 0)
    return [m[k] for k in sorted(m)]
