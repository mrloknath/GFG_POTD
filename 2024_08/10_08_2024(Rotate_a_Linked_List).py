class Solution:
    def rotate(self, head, k):
        current = head
        reversedPart = None  
        remainingRotations = k
        lastNode = head
        
        while lastNode.next is not None:
            lastNode = lastNode.next
        while remainingRotations != 0 and current is not None:
            nextNode = current.next 
            head = nextNode  
            current.next = reversedPart  
            lastNode.next = current  
            lastNode = lastNode.next  
            current = nextNode  
            remainingRotations -= 1  
        return head  
