#Author : Loknath Giri

class Solution:
    head=None
    def LLtoS(self,num):
        strn='0'
        while(num):
            strn=strn+str(num.data)
            num = num.next
        return strn
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        s1=self.LLtoS(num1)
        s2=self.LLtoS(num2)
        sum=int(s1)+int(s2)
        s3=reversed(str(sum))
        for i in s3:
            self.insertAtBegin(int(i))
        return self.head
            
