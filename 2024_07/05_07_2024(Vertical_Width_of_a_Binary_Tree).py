def verticalWidth(root):
    # code here
    if not root:
        return 0
    distance = set()
    q = deque([(root, 0)])
    while q:
        node, hw = q.popleft()
        distance.add(hw)
        if node.left:
            q.append((node.left, hw - 1))
        if node.right:
            q.append((node.right, hw + 1))
    return len(distance)
