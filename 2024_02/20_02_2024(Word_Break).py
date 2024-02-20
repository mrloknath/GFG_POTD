class Node:
    def __init__(self):
        self.next = {}
        self.end = 0

def insert(x, root):
    node = root
    
    for i in x:
        if i in node.next:
            node = node.next[i]
        else:
            new_node = Node()
            node.next[i] = new_node
            node = new_node
    
    node.end += 1

class Solution:
    def wordBreak(self, A, B):
        root = Node()
        
        for i in B:
            insert(i, root)
        
        n = len(A)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n - 1, -1, -1):
            node = root
            for j in range(i, n):
                if A[j] not in node.next:
                    break
                
                node = node.next[A[j]]
                
                if node.end > 0 and dp[j + 1]:
                    dp[i] = True
                    break
        
        return dp[0]
