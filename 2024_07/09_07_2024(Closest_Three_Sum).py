class Solution:
    def threeSumClosest (self, arr, target):
        arr.sort()
        minDiff = float('inf')
        closest_sum = 0
        
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue 
            l, r = i + 1, len(arr) - 1
            while l < r:
                current_sum = arr[i] + arr[l] + arr[r]
                if current_sum == target:
                    return current_sum 
                
                current_diff = abs(current_sum - target)
                if current_diff < minDiff:
                    minDiff = current_diff
                    closest_sum = current_sum
                elif current_diff == minDiff:
                    closest_sum = max(closest_sum, current_sum)
                
                if current_sum < target:
                    l += 1
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1  
                else:
                    r -= 1
                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1 
        
        return closest_sum
