class Solution:
    def delete_node(self, head, x):
        current = head

        if x == 1:
            if not head.next:return None
            current, current.prev = current.next, None
            return current

        for _ in range(x - 1):
            current = current.next
            if not current:return head

        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next

        return head
