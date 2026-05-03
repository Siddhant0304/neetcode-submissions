class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i,curSum, curList):
            if curSum == target: 
                res.append(curList[:])
                return
            if curSum > target or i>=n:
                return
            
            # curSum += nums[i]
            # curList.append(nums[i])
            backtrack(i,curSum + nums[i],curList + [nums[i]])
            # curSum -= nums[i]
            # curList.remove(nums[i]) 
            backtrack(i+1,curSum , curList )
            return

          
        backtrack(0, 0, [])


        return res
         