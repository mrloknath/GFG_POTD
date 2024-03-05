class Solution:
    def maxIndexDiff(self, a, n):
        preMin = [0] * n
        suffMax = [0] * n

        maxi = a[n - 1]
        for i in range(n - 1, -1, -1):
            maxi = max(maxi, a[i])
            suffMax[i] = maxi

        mini = a[0]
        for i in range(n):
            mini = min(mini, a[i])
            preMin[i] = mini

        i = 0
        j = 0
        ans = -1
        while i < n and j < n:
            if preMin[i] <= suffMax[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans
