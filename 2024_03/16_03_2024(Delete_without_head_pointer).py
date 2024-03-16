class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        #code here
        if del_node.next is None:
            temp = del_node
            del_node = None
            del temp
            return
        del_node.data, del_node.next.data = del_node.next.data, del_node.data
        temp = del_node.next
        del_node.next = del_node.next.next
        del temp
