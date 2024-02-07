def count_k_dist_nodes(root, k, level, map, unique_nodes):
    if not root:
        return
    
    level += 1
    map[level] = root
    if root.left is None and root.right is None:
        if level >= k+1:
            unique_nodes.add(map.get(level-k))
    
    count_k_dist_nodes(root.left, k, level, map, unique_nodes)
    count_k_dist_nodes(root.right, k, level, map, unique_nodes)
    
    
class Solution:
    def printKDistantfromLeaf(self, root, k):
        #code here
        if not root:
            return 0
    
        unique_nodes = set()
        map = {}
        level = 0
        count_k_dist_nodes(root, k, level, map, unique_nodes)
        return len(unique_nodes)
