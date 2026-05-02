class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)

        l,r  = 0,1

        while r <= n-1:
            maxprofit = max(maxprofit, prices[r]-prices[l])
            
            if r==n-1:
                l+=1
                r=l+1
            else:
                r+=1
                
        
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         maxprofit = max(maxprofit, prices[j]-prices[i])

        return maxprofit
