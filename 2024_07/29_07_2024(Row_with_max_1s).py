class Solution:
    def rowWithMax1s(self, arr):
        #
        max_count, max_index = 0, -1
        for i in range(len(arr)):
            if arr[i][-1] > max_count:
                max_count = arr[i][-1]
                max_index = i
            elif arr[i][-1] == max_count:
                max_index = i if sum(arr[i]) > sum(arr[max_index]) else max_index
        return max_index
