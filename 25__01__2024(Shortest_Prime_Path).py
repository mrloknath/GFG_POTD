class Solution:
    def solve (self,Num1,Num2):
        max_num = 9999
        prime = [1]*10001
        prime[1] = 0
        for i in range(2, int(max_num**0.5) + 1):
            if prime[i]:
                for j in range(i*i, max_num + 1, i):
                    prime[j] = 0
        dp = [-1] * 10001
        vis = [0] * 10001
        q = []
        q.append(Num1)
        dp[Num1] = 0
        vis[Num1] = 0
        while q:
            current = q.pop(0)
            if vis[current]:
               continue
            vis[current] = 1
            s = str(current)
            for i in range(4):
                for ch in range(10):
                    ch = str(ch)
                    if ch == s[i] or (ch == '0' and i == 0): 
                        continue
                    next = list(s)
                    next[i] = ch
                    next_num = int(''.join(next))
                    if prime[next_num] and dp[next_num] == -1:
                        dp[next_num] = 1 + dp[current]
                        q.append(next_num)
                    if next_num == Num2:
                        return dp[next_num]
        return dp[Num2]
