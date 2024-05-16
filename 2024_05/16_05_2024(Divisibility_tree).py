from typing import List

class Solution:
    ans = 0
    
    def dfs(self, adj, vis, start):
        vis[start] = 1
        cnt = 0
        for neighbor in adj[start]:
            if not vis[neighbor]:
                res = self.dfs(adj, vis, neighbor)
                if res % 2 == 0:
                    self.ans += 1
                else:
                    cnt += res
        return cnt + 1
        
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0] - 1].append(edge[1] - 1)
            adj[edge[1] - 1].append(edge[0] - 1)    
        vis = [0] * n
        self.dfs(adj, vis, 0)
        return self.ans
        
