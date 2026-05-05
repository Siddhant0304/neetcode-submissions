class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True

        for i in range(n-2,-1,-1):
            end = min(i+nums[i]+1,n)
            for j in range(i+1, end):
                if dp[j] == True:
                    dp[i] = True
                    break
        
        return dp[0]


        # def f(i):
        #     if i in dp: return dp[i]
        #     if i == n-1: return True
        
        #     if nums[i]== 0: return False
        #     end = min(len(nums)m i+nums[i])
        #     for j in range(i+1, end):
        #         if f(j) == True: 
        #             dp[i] = True
        #             return True
            
        #     dp[i] = False
        #     return False

        # return f(0)
        