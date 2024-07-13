from typing import List
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj = [[] for _ in range(n + 1)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        V = n
        S = 1
        destination = V
        parent = [i for i in range(V + 1)]
        path = []
        q = []
        distance = [float('inf')] * (V + 1)
        distance[S] = 0
        parent[S] = S
        heapq.heappush(q, (0, S))

        while q:
            dis, node = heapq.heappop(q)
            for neighbor, wt in adj[node]:
                if dis + wt < distance[neighbor]:
                    distance[neighbor] = dis + wt
                    heapq.heappush(q, (distance[neighbor], neighbor))
                    parent[neighbor] = node

        node = destination
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        if distance[destination]==float('inf'):
            return [-1]
        path.append(S)
        total_distance = distance[destination]
        return [total_distance] + path[::-1]

        
