class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high  = 0, n-1
        if n==1: return nums[0]
        while nums[low] > nums[high]:
            mid = (low+high)//2 
            if nums[mid] > nums[high]: 
                low = mid+1
            else:
                high = mid
                
        return nums[low]


        # if nums[0] <= nums[n-1]: return nums[0]
        
        # for i in range(n-1,-1,-1):
        #     if nums[i]<nums[i-1]: return nums[i]
        