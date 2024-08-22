from typing import List

class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        from collections import defaultdict
        adj=defaultdict(set)
        ind=defaultdict(int)
        char=set()
        for ix,ve in enumerate(alien_dict):
            if ix+1==N:
                continue
            cur=list(ve)
            nxt=list(alien_dict[ix+1])
            char.update(cur+nxt)
            for a,b in zip(cur,nxt):
                if a==b:
                    continue
                if b not in adj[a]:
                    ind[b]+=1
                    adj[a].add(b)
                break
        q=[]
        for c in char:
            if ind[c]==0:
                q.append(c)
        ret=[]
        while q:
            cur=q.pop()
            ret.append(cur)
            for nxt in adj[cur]:
                ind[nxt]-=1
                if ind[nxt]==0:
                    q.append(nxt)
        return ret
        
