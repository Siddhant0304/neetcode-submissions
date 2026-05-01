class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):
            diff  = target - nums[i]
            if diff in map:
                return [map[diff],i]
            map[nums[i]] = i

            
        # for i in range(len(nums)):
        #     diff = target-nums[i]
        #     if diff in nums[i+1:]:
        #         ind = nums[i+1:].index(diff)
        #         return [i,ind+i+1]


        
       


