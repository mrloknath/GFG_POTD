class Solution:
    def absolute_diff(self, root):
        # Your code here
        ans = float('inf')
        stack = []
        curr = root
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev:
                ans = min(ans, abs(prev.data - curr.data))
            prev = curr
            curr = curr.right
        return ans
