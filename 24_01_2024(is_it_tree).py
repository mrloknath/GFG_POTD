class Solution:
    def isTree(self, n, m, edges):
    #Code here
        adj=[[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        vis=set()
        q=[(0,-1)]
        while q:
            p=q.pop()
            vis.add(p[0])
            for i in adj[p[0]]:
                if i not in vis:
                    q.append((i,p[0]))
                elif i!=p[1]:
                    return 0
        if len(vis)==n:
            return 1
        else:
            return 0
