from typing import List

class Solution:
    def findMissing(self, a: List[int], b: List[int], n: int, m: int) -> List[int]:
        st = set(b)
        ans = []
        
        for num in a:
            if num not in st:
                ans.append(num)
                
        return ans
