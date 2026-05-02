class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        
        for i in range(n-1):
            for j in range(i+1,n):
                maxprofit = max(maxprofit, prices[j]-prices[i])

        return maxprofit
