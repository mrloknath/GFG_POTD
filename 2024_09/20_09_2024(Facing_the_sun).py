class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        n = len(height)
        ans = 1
        curr_max = height[0]
        for i in range(1, n):
            if height[i] > curr_max:
                ans = ans +1
                curr_max = height[i]
        return ans
