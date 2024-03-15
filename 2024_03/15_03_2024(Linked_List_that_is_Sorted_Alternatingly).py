class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, h1):
        s = Node(0)
        d = Node(0)
        w = s
        while h1:
            w.next = h1
            w = w.next
            h1 = h1.next
            w.next = None
            if h1:
                t = h1.next
                h1.next = d.next
                d.next = h1
                h1 = t
        w.next = d.next
        return s.next

