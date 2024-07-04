class Solution:
    def printAllDups(self, root):
        # code here
        from collections import Counter
        counter = Counter()
        ans = []
        def walk(n):
            if not n:
                return None
            l = walk(n.left)
            r = walk(n.right)
            tree = (n.data, l, r)
            counter[tree] += 1
            if counter[tree] == 2:
                ans.append(n)
            return tree
            
        walk(root)
        return sorted(ans, key=lambda x: x.data)
