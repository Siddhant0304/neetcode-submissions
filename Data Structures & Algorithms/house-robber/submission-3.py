class Solution:
    def rob(self, nums: List[int]) -> int:
        #tabulation
        n= len(nums)
        dp = [-1]*n
        dp[0] = nums[0]

        for i in range(1,n):
            if i==1:
                pick = nums[i]
            else:
                pick = nums[i] + dp[i-2]
            notpick = dp[i-1]
            dp[i] = max(pick, notpick)

        return dp[n-1]
        # memoization
        # n = len(nums)
        # arr = [0]*n
        # def dfs(ind):
        #     if ind == 0 : 
        #         return nums[ind]
        #     if arr[ind] != 0: return arr[ind]
        #     if ind < 0: return 0
        #     pick = nums[ind] + dfs(ind-2)
        #     notpick = dfs(ind-1)
        #     arr[ind] = max(pick,notpick)
        #     return max(pick,notpick)
        
        # return dfs(n-1)