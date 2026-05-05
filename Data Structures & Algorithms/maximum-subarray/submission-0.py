class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n)
        dp[0] = max(0,nums[0])
        maxSum = nums[0]

        for i in range(1,n):
            if dp[i-1] + nums[i] < 0:
                maxSum = max(nums[i],maxSum)
            else:
                dp[i] = dp[i-1]+nums[i]
                maxSum = max(dp[i],maxSum)

        return maxSum