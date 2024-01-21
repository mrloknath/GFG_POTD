from typing import List


class Solution:
    def checkCover(self, n, k, m, adj):
        sett = (1 << k) - 1
        limit = (1 << n)
        while (sett < limit):
            visited = [[False for i in range(n+1)] for j in range(n+1)]
            cnt = 0
            j = 1
            v = 1
            while(j < limit):
                if (sett & j):
                    for k in range(1, n+1):
                        if(adj[v][k] and (not visited[v][k])):
                            visited[v][k] = 1
                            visited[k][v] = 1
                            cnt = cnt + 1
                j = j << 1
                v = v + 1
            if (cnt == m):
                return True
            c = sett & -sett
            r = sett + c
            sett = (((r ^ sett) >> 2) // c) | r
        return False
    
    def vertexCoverHelper(self, adj, n, m):
        low = 1
        high = n
        while (high > low):
            mid = (low + high) >> 1
            if(self.checkCover(n, mid, m, adj) == False):
                low = mid + 1
            else:
                high = mid
        return low
        
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        m = len(edges)
        rows, cols = n+1, n+1
        adj = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(m):
            adj[edges[i][0]][edges[i][1]] = 1
            adj[edges[i][1]][edges[i][0]] = 1
        return self.vertexCoverHelper(adj, n, m)
