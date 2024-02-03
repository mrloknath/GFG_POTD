class Solution:
    def decimalValue(self, head):
            MOD=10**9+7
            # Code here
            b=[]
            p=head
            while p:
                b.append(p.data)
                p=p.next            
            n=len(b)
            ans,pwr=0,n-1
            for i in b:
                ans+=(i*2**pwr)%MOD
                pwr-=1
            return ans%MOD
