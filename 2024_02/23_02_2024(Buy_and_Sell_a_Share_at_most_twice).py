class Solution:
    def maxProfit(self, n,prices: List[int]) -> int:
        #n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        
        for index in range(n - 1, -1, -1):
            for buy in range(2):
                for limit in range(1, 3):
                    if buy == 1:
                        buyit = -prices[index] + dp[index + 1][0][limit]
                        skip = 0 + dp[index + 1][1][limit]
                        dp[index][buy][limit] = max(buyit, skip)
                    else:
                        sell = prices[index] + dp[index + 1][1][limit - 1]
                        skip = 0 + dp[index + 1][0][limit]
                        dp[index][buy][limit] = max(sell, skip)
        
        return dp[0][1][2]
