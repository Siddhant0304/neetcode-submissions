from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # if k == len(nums): return nums
        # c = Counter(nums)
        # freqItems = c.most_common(k)
        # res = []
        # for key,val in freqItems:
        #     res.append(key)
        
        # return res
        
        freqMap = {}
       
        for num in nums:
            if num in freqMap:
                freqMap[num]+=1
            else:
                freqMap[num]=1
        
        lis = sorted(freqMap.items(), reverse= True, key= lambda x: x[1])
        return [ key for key, val in lis[:k]]
        
        
        

        