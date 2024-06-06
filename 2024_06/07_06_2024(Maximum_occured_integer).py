class Solution:
    # Complete this function
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        freq = [0] * (maxx + 2)
        for i in range(n):
            freq[l[i]] += 1
            freq[r[i] + 1] -= 1
        max_count = 0
        max_occuring_element = 0
        current_count = 0
        for i in range(maxx + 1):
            current_count += freq[i]
            if current_count > max_count:
                max_count = current_count
                max_occuring_element = i
        return max_occuring_element
