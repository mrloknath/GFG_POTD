class Solution:
    def findSmallestMaxDist(self, stations, K):
        # Code here
        start, end = 0, stations[-1] - stations[0]
        while end - start > 1e-5:
            mid = (start + end)/2   # our guess (max distance)
            if self.isPossible(stations, K, mid):
                end = mid
            else:
                start = mid
        return end
    
    
    def isPossible(self, stations, k, maxDist):
        stationsToAdd = 0
        for i in range(1, len(stations)):
            stationsToAdd += (stations[i] - stations[i-1])//maxDist
        return stationsToAdd <= k
