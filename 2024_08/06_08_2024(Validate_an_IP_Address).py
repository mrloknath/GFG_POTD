class Solution:
    def isValid(self, str):
        #code here
        x=str.split('.')
        if len(x)!=4:
            return False
        for i in x:
            if(i!=''):    #  if not an empty string
                if(int(i)<0 or (i[0]=='0' and len(i)>1) or int(i)>255):
                  return False
            else:
                return False
        return True

 
