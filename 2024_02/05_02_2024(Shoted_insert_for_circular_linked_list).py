class Solution:
    def sortedInsert(self, head, data):
        #code here
        new_node = Node(data)
        if not head:
            new_node.next = new_node
            return new_node
        if data < head.data:
            temp = head
            while temp.next != head:
                temp = temp.next
            temp.next = new_node
            new_node.next = head
            return new_node
        current = head
        while current.next != head and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head
