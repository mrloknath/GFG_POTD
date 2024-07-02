from collections import deque
def convert(head):
    root=Tree(head.data)
    q=deque()
    q.append(root)
    head=head.next
    while head:
        temp=q.popleft()
        temp.left=Tree(head.data)
        q.append(temp.left)
        head=head.next
        if head:
            temp.right=Tree(head.data)
            q.append(temp.right)
            head=head.next
    return root
