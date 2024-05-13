from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        parent = list(range(v))
        
        def find(x: int) -> int: #DSU-find parent
            if parent[x]==x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        degree = [0]*v
        for x,y in edges:
            degree[x-1] += 1
            degree[y-1] += 1
            parent[find(x-1)] = find(y-1)
        group = defaultdict(list)
        for i in range(v): group[find(i)].append(i)
        return sum(all(degree[x]==len(comps)-1 for x in comps) for comps in group.values())
