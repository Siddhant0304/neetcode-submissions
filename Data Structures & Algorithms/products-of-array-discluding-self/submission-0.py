class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, res= [0]*n,[0]*n,[0]*n
        numl, numr = 1,1
        for i in range(n):
            numl *= nums[i]
            left[i] = numl
        
        for i in range(n-1,-1, -1):
            numr *= nums[i]
            right[i] = numr
        

        for i in range(n):
            if i == 0:
                res[i]=right[i+1]
            elif i == n-1:
                res[i] = left[i-1]
            else:
                res[i] = left[i-1] * right[i+1]
      
        return res