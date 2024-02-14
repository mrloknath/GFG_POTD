class Solution:
    def dfs(self, u, parent, time, disc, low, visited, result, adj):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in adj[u]:
            if not visited[v]:
                self.dfs(v, u, time, disc, low, visited, result, adj)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    # Edge u-v is a critical connection
                    result.append([min(u, v), max(u, v)])
            elif v != parent:
                low[u] = min(low[u], disc[v])

    def criticalConnections(self, v, adj):
        result = []
        disc = [-1] * v
        low = [-1] * v
        visited = [False] * v
        time = [0]

        for i in range(v):
            if not visited[i]:
                self.dfs(i, -1, time, disc, low, visited, result, adj)

        result.sort()
        return result
