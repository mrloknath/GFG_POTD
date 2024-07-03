class Solution:
    def removeAllDuplicates(self, head):
        # code here
        dic = dict()
        temp=head
        while temp:
            if temp.data not in dic:
                dic[temp.data]=1
            else:
                dic[temp.data]+=1
            temp=temp.next
        temp=head
        head2=Node(1)
        temp2=head2
        while temp:
            if dic[temp.data]<=1:
                x=Node(temp.data)
                temp2.next=x
                temp2=x
            temp=temp.next
        head2=head2.next
        return head2
