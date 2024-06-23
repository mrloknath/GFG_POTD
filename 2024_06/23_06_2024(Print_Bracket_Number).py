class Solution:
	def bracketNumbers(self, str):
		# code here
		o=0
        c=0
        l=[]
        r=[]
        for i in str:
            if i=="(":
                o+=1
                l.append(o)
                r.append(o)
            if i==")":
                c=l.pop()
                r.append(c)
        return r
