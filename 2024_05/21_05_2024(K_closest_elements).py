class Solution:
    def findCrossOver(self, arr, low, high, x):
        # Base cases
        if arr[high] <= x:
            return high
        if arr[low] > x:
            return low
        
        mid = (low + high) // 2
        
        # Check if mid is the crossover point
        if arr[mid] <= x and arr[mid + 1] > x:
            return mid
        elif arr[mid] < x:
            return self.findCrossOver(arr, mid + 1, high, x)
        return self.findCrossOver(arr, low, mid - 1, x)

    def printKClosest(self, arr, n, k, x):
        id1 = self.findCrossOver(arr, 0, n - 1, x)
        
        # Move forward
        id2 = id1 + 1
        
        # If element is present then we have to neglect
        if id1 >= 0 and arr[id1] == x:
            id1 -= 1
        
        ans = []
        for _ in range(k):
            # Both pointing at valid index
            if id1 >= 0 and id2 < n:
                val1 = x - arr[id1]
                val2 = arr[id2] - x
                # val1 is more closest (diff is smaller)
                if val1 < val2:
                    ans.append(arr[id1])
                    id1 -= 1
                else:
                    # val2 is more closest or if same we prioritize the greater number
                    ans.append(arr[id2])
                    id2 += 1
            elif id1 >= 0:
                ans.append(arr[id1])
                id1 -= 1
            else:
                ans.append(arr[id2])
                id2 += 1
        
        return ans
