from heapq import heappop, heappush, heapify
class Solution:
    def minCost(self, arr):
        cost = 0
        h = arr
        heapify(h)
        while len(h) > 1:
            p1 = heappop(h)
            p2 = heappop(h)
            cost += p1+p2
            heappush(h, p1+p2)
        return cost
