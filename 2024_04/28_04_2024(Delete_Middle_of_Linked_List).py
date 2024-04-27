class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        
        #code here
        if not head or not head.next:  # If the linked list is empty or contains a single node
            return None
        
        # Find the middle node using slow and fast pointers
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        prev.next = slow.next
        
        return head
    
