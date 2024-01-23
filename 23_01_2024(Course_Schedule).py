from collections import deque

class Solution:
    def findOrder(self, n, m, prerequisites):
        g = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for edge in prerequisites:
            g[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1
        
        q = deque()
        ans = []
        
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
                ans.append(i)
        
        while q:
            node = q.popleft()
            
            for child in g[node]:
                in_degree[child] -= 1
                
                if in_degree[child] == 0:
                    q.append(child)
                    ans.append(child)
        
        if len(ans) < n:
            ans = []
            
        return ans

# Driver Code
def check(V, res, adj):
    _map = [-1] * V
    for i in range(V):
        _map[res[i]] = i
    
    for i in range(V):
        for v in adj[i]:
            if _map[i] > _map[v]:
                return 0
    
    return 1
