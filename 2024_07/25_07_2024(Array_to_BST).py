class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.buildBST(nums, 0, len(nums) - 1)
        
    def buildBST(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Node(nums[mid])
        node.left = self.buildBST(nums, left, mid - 1)
        node.right = self.buildBST(nums, mid + 1, right)
        return node
