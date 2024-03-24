#Author : Loknath Giri



#Solution 1 : using + operator on list concatination
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        listX=[x]
        return listX + st




#Solution 2 : Using list.extend()
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        listX=[x]
        listX.extend(st)
        return listX 
