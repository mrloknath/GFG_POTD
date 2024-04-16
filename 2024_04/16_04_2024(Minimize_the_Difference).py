from typing import List


class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        post_max = [0] * n
        post_min = [0] * n
        post_max[n - 1] = arr[n - 1]
        post_min[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            post_max[i] = max(arr[i], post_max[i + 1])
            post_min[i] = min(arr[i], post_min[i + 1])

        ans = post_max[k] - post_min[k]

        maxi = arr[0]
        mini = arr[0]

        for i in range(1, n - k):
            ans = min(ans, max(post_max[i + k], maxi) - min(post_min[i + k], mini))

            maxi = max(arr[i], maxi)
            mini = min(arr[i], mini)

        ans = min(ans, maxi - mini)

        return ans
