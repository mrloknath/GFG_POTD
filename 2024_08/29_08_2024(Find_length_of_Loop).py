class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head  
        count=1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow.next != fast:
                    slow = slow.next
                    count += 1
                return count
        else:
          return 0
