class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            n = nums[i]
            if target-n in nums[i+1:]:
                return [i, nums[i+1:].index(target-n)+i+1]


        
       


