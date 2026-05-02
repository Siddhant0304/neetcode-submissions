class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)

        l, r = 0,1  #l = buyleft, r = sellright

        while r <= n-1:
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, prices[r]-prices[l])

            else:
                l = r 
            
            r+=1
            
            
                 
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         maxprofit = max(maxprofit, prices[j]-prices[i])

        return maxprofit
