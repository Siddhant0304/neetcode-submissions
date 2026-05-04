class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        arr = [0]*n
        def dfs(ind):
            if ind == 0 : 
                return nums[ind]
            if arr[ind] != 0: return arr[ind]
            if ind < 0: return 0
            pick = nums[ind] + dfs(ind-2)
            notpick = dfs(ind-1)
            arr[ind] = max(pick,notpick)
            return max(pick,notpick)
        
        return dfs(n-1)