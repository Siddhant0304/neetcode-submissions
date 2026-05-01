from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict()

        for num in nums:
            if num in map:
                return True
            else:
                map[num]=1
        
        return False