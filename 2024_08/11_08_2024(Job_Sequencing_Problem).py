class Solution: 
    def JobScheduling(self,Jobs,n):
        sorted_Jobs = sorted(Jobs,key=lambda x: x.profit, reverse=True)
        timeline = [-1]*n
        sm_ct,ct = 0,0
        
        for i in sorted_Jobs:
            
            idx = i.deadline-1
            
            while idx >= 0 and timeline[idx] != -1: idx -= 1
            
            if idx >= 0:
                
                timeline[idx] = i.id
                sm_ct,ct = sm_ct+i.profit,ct+1
                
        return [ct,sm_ct]
