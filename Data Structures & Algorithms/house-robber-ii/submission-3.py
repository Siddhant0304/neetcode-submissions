class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]

        def linearRob(arr):
            n = len(arr)
            dp = [-1]*n

            #tabulate
            dp[0] = arr[0] 

            for i in range(1,n):
                pick = arr[i]
                if i>1:
                    pick += dp[i-2]
                notpick = dp[i-1]
                dp[i] = max(pick, notpick)
            return dp[n-1]
            
            # def f(i):
            #     if i==0: return arr[0]
            #     if dp[i] != -1: return dp[i]
            #     if i < 0: return 0
        
            #     pick = arr[i] + f(i-2)     
            #     notpick = f(i-1)

            #     dp[i] = max(pick,notpick)
            #     return dp[i]
            # return f(n-1)
             
        n = len(nums)   
        nums1,nums2 = nums[1:],nums[:n-1]
        return max(linearRob(nums1), linearRob(nums2))
        
