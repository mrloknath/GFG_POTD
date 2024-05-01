#Author : Lolknath Giri

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        v=['a','e','i','o','u']
        vn=Node(0)
        cn=Node(0)
        visit=head
        head=vn
        chead=cn
        while visit:
            new_node=Node(visit.data)
            if new_node.data in v:
                vn.next=new_node
                vn=vn.next
            else:
                cn.next=new_node
                cn=cn.next
            visit=visit.next
        vn.next=chead.next    
        return head.next
