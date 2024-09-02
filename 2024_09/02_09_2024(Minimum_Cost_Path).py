class Solution:
    def minimumCostPath(self, grid):
		#Code here
		from heapq import heappush, heappop
		INF = float('inf')
		m, n = len(grid), len(grid[0])
		seen = set()
		q = [(grid[0][0], (0, 0))]
		while q:
		    cost0, (r, c) = heappop(q)
		    if (r, c) in seen:
		        continue
		    if r == m-1 and c == n-1:
		        return cost0
		    seen.add((r, c))
		    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
		        if 0 <= nr < m and 0 <= nc < n:
		            heappush(q, (cost0+grid[nr][nc], (nr, nc)))
	    return -1
	    
