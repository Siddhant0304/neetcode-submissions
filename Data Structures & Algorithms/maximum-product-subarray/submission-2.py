class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxprod, minprod = [-1] * n, [-1] * n
        maxprod[0] = minprod[0] = nums[0]
        ans = nums[0]
        for i in range(1,n):
            maxprod[i] = max(maxprod[i-1]*nums[i], minprod[i-1]*nums[i], nums[i])
            minprod[i] = min(maxprod[i-1]*nums[i], minprod[i-1]*nums[i], nums[i])
            ans = max(ans, maxprod[i])
  
        return ans


        