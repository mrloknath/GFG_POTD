#User function Template for python3
class Solution:
    def largestBst(self, root):
        # Your code here
        def walk(n):
            if not n:
                return True, 0, float('inf'), float('-inf')
            lf, lsize, lmin, lmax = walk(n.left)
            rf, rsize, rmin, rmax = walk(n.right)
            
            if lf and rf and lmax < n.data < rmin:
                return True, 1+lsize+rsize, min(n.data, lmin), max(n.data, rmax)
            
            return False, max(lsize, rsize), 0, 0
        
        _, r, _, _ = walk(root)
        return r
