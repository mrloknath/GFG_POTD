class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        dic = {}
        temp = head1
        while temp != None:
            dic[temp.data] = 1
            temp = temp.next
        count = 0
        while head2 != None:
            req = x - head2.data
            if req in dic:
                count += 1
            head2 = head2.next
        
        return count
        
