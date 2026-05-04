class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp  = [-1] * (amount+1)
        dp[0] = 0
       
        for i in range(1,amount+1):
            minCoins = float('inf')
            
            for c in coins:
                if c <= i:
                    remainder = i - c 
                    if dp[remainder] != -1:
                        minCoins = min(1 + dp[remainder], minCoins)

                dp[i] = minCoins

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

        

        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     if amount < 0 : return float('inf')
        #     minCoins = float('inf')
        #     for c in coins:
        #         minCoins =  min(minCoins, 1 + dfs(amount-c))
        #     return minCoins
        
        # res = dfs(amount)
        # return res if res != float('inf') else -1

        # n = len(coins)
        # dp = [[-1]*(amount+1) for _ in range(n)]
   
        # def helper(i, total):
        #     if dp[i][total] != -1: return dp[i][total]
        #     if i == 0:
        #         if total%coins[0]==0: return total//coins[0]
        #         else: return float('inf')
        #     if i<=-1:
        #         return 0
            
        #     pick = float('inf')
        #     if total >= coins[i]:
        #         pick = 1 + helper(i, total-coins[i])
        #     notpick = helper(i-1,total)
        #     dp[i][total] = min(pick, notpick)
        #     return dp[i][total]
        
        # a =helper(len(coins)-1,amount)
        # if a == float('inf'): 
        #     return -1
        # else:
        #     return a