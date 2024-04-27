class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def merge(self, left, right, isIncreasing):
        if left is None:
            return right
        if right is None:
            return left
        
        if isIncreasing:
            if left.data < right.data:
                left.next = self.merge(left.next, right, True)
                left.next.prev = left
                left.prev = None
                return left
            else:
                right.next = self.merge(left, right.next, True)
                right.next.prev = right
                right.prev = None
                return right
        else:
            if left.data > right.data:
                left.next = self.merge(left.next, right, False)
                left.next.prev = left
                left.prev = None
                return left
            else:
                right.next = self.merge(left, right.next, False)
                right.next.prev = right
                right.prev = None
                return right
                
    def split(self, head):
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None
        middle.prev = None
        
        return head, middle
    
    def sortDoubly(self, head):
         #Your code here
        if head is None or head.next is None:
            return head
        
        left, right = self.split(head)
        
        left = self.sortDoubly(left)
        right = self.sortDoubly(right)
        
        return self.merge(left, right, True)  # Only return one sorted list for non-decreasing order
    
