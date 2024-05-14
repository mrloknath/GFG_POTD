from typing import List
import heapq

class Solution:
    def MinimumEffort(self, n: int, m: int, heights: List[List[int]]) -> int:
        #code here
        pq = [(0, 0, 0)]  # (step, row, col)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        while pq:
            step, row, col = heapq.heappop(pq)
            
            if row == n - 1 and col == m - 1:
                return step
            
            for nrow, ncol in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= nrow < n and 0 <= ncol < m:
                    val = max(step, abs(heights[nrow][ncol] - heights[row][col]))
                    if val < dist[nrow][ncol]:
                        dist[nrow][ncol] = val
                        heapq.heappush(pq, (val, nrow, ncol))
        
        return dist[n-1][m-1]
