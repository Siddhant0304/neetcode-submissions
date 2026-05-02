class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            diff = -nums[i]
            j,k = i+1, n-1
            while j<k:
                if nums[j]+nums[k] == diff:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k] < diff: 
                    j+=1
                else:k-=1

        return list(res)
            


        