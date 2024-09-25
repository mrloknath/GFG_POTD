class Solution:
    def isPalindrome(self, head):
        #code here
        temp=head
        curr=head
        prev=None
        while curr is not None:
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        reverse_head=prev
        while temp:
            if reverse_head.data!=temp.data:
                return False
            temp=temp.next
            reverse_head=reverse_head.next
        return True
