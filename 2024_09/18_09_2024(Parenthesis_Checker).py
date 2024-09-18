class Solution:
    def ispar(self,x):
        # code here
        st = []
        for e in x:
            if e in '([{':
                st.append(e)
            else:
                if not st or st.pop()+e not in ["()", "[]", "{}"]:
                    return False
        return len(st) == 0
