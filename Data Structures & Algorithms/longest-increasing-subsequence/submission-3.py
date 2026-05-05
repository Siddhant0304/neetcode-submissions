class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n= len(nums)
        # dp = [[-1]*(n+1) for _ in range(n)] 
        # def dfs(i, last):
        #     if i>=n: return 0
        #     if dp[i][last+1] !=-1: return dp[i][last+1]
        #     pick = 0
        #     if last == -1 or nums[i]>nums[last]:
        #         pick = 1 + dfs(i+1,i)
        #     notpick = dfs(i+1,last)
        #     dp[i][last+1]=max(pick,notpick)
        #     return dp[i][last+1]
        
        # return dfs(0,-1)

        n = len(nums)
        dp = [1]*(n)
        maxAll = 1
        dp[0] =1

        for i in range(1,n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i]= max(dp[i], dp[j]+1)
                
            maxAll = max(dp[i], maxAll)
        
        return maxAll

        
        

        