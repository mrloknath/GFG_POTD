#Author : Loknath Giri

class Solution:
    def removeDuplicates(self,s):
        ans=""
        while s!="":
            sc=s[0];
            s=s.replace(sc,"")
            ans=ans+sc
        return ans
