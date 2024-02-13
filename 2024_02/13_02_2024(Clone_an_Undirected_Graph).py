import sys
sys.setrecursionlimit(10**6)
class Solution():
    def cloneGraph(self, node):
#your code goes here
        d={}
        def util(nod):
            if not nod:
                return None
            if nod.val in d:
                return d[nod.val]
            d[nod.val]=Node(nod.val, []) 
            for n in nod.neighbors:
                d[nod.val].neighbors.append(util(n))
            return d[nod.val]
        return util(node)
