class Solution:
    def findMaxDiff(self, arr):
        # code here
        n = len(arr)
        stack = []
        left,right = [0]*n, [0]*n
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(arr[i])
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(arr[i])
        
        return max(abs(left[i]-right[i]) for i in range(n))
