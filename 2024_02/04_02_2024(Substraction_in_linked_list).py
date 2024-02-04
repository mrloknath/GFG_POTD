class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        sum1 = 0
        sum2 = 0
        
        while l1 is not None:
            sum1 = sum1 * 10 + l1.data
            l1 = l1.next
            
        while l2 is not None:
            sum2 = sum2 * 10 + l2.data
            l2 = l2.next
        node = Node(abs(sum1 - sum2))

        return node
