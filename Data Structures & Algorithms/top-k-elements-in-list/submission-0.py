from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums): return nums
        c = Counter(nums)
        freqItems = c.most_common(k)
        res = []
        for key,val in freqItems:
            res.append(key)
        
        return res
        



        # freqMap = {}
       
        # for num in nums:
        #     if num in freqMap:
        #         freqMap[num]+=1
        #     else:
        #         freqMap[num]=1

        # maxHeap = [-1*x for x in freqMap.values()]
        # heapq.heapify(maxHeap)

        # cnt = k
        # res = []

        # while (cnt):
        #     curVal = -1* heapq.heappop(maxHeap)
        #     for key,val in freqMap.items():
        #         if cnt == 0: return res
        #         if val == curVal and cnt > 0:
        #             res.append(key)
        #             cnt-=1
            


        
        

        