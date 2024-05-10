class Solution:
    def solve(self, ind, n, target, nums, temp, ans):
        if target == 0:
            ans.append(list(temp))
            return
        for i in range(ind, n):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            temp.append(nums[i])
            self.solve(i + 1, n, target - nums[i], nums, temp, ans)
            temp.pop()
    def CombinationSum2(self, arr, n, k):
        # code here
        arr.sort()
        ans = []
        temp = []
        self.solve(0, n, k, arr, temp, ans)
        return ans
