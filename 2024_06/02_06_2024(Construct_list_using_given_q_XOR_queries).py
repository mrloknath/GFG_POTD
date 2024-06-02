from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # code here
        xr,lis=0,[]
        while queries:
            a,b=queries.pop();
            if a==0:
                lis.append(b^xr)
            else:
                xr^=b
        lis.append(xr)        
        return sorted(lis)    
