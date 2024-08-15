class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        itr=head
        lst=[]
        count=0
        while itr:
            lst.append(itr.data)
            itr=itr.next
        s="".join(map(str,lst))
        num=int(s)+1
        new_head = Node(int(str(num)[0]))
        current = new_head
        for digit in str(num)[1:]:
            current.next = Node(int(digit))
            current = current.next
        return new_head
