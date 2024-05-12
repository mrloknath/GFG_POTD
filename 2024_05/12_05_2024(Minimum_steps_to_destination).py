class Solution:
    def minSteps(self, d):
        # code here
        c=0
        s=0
        while c<d:
            s+=1
            c+=s
        while (c-d)%2!=0:
            s+=1
            c+=s
        return s
