import heapq

class Solution:
    def minValue(self, s: str, k: int) -> int:
        f = [0] * 26
        for i in s:
            f[ord(i) - ord('a')] += 1

        pq = []
        for i in f:
            if i:
                heapq.heappush(pq, -i)

        while k > 0 and len(pq) > 0:
            x = -heapq.heappop(pq)
            x -= 1

            if x > 0:
                heapq.heappush(pq, -x)
                
            k -= 1

        ans = 0
        while len(pq) > 0:
            x = -heapq.heappop(pq)
            ans += x * x

        return ans
