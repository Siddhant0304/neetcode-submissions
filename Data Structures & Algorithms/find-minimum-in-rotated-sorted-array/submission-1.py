class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        if nums[0] <= nums[n-1]: return nums[0]
        
        for i in range(n-1,-1,-1):
            if nums[i]<nums[i-1]: return nums[i]
        