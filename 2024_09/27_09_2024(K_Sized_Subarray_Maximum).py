class Solution:
      #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, k, arr):
        from heapq import heappop, heappush
        h = []
        for i in range(k - 1):
            heappush(h, (-arr[i], i))
        ans = []
        for i in range(k - 1, len(arr)):
            heappush(h, (-arr[i], i))
            while h[0][1] <= i - k:
                heappop(h)
            ans.append(-h[0][0])
        return ans
