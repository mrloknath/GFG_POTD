class Solution:
    def deleteK(self, head, k):
        #code here  
        if k == 1:
            return None
        
        counter = 0
        prev = None
        cur = head
        while cur is not None:
            if counter == k - 1:
                prev.next = cur.next
            prev = cur
            cur = cur.next
            counter = (counter + 1) % k
        
        return head
