class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        from collections import defaultdict
        
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = set([src])
        q = [src]
        ans = [-1]*n
        d = 0
        while q:
            nq = []
            for e in q:
                ans[e] = d
                for nbr in g[e]:
                    if nbr not in visited:
                        nq.append(nbr)
                        visited.add(nbr)
            q = nq
            d += 1
        return ans
