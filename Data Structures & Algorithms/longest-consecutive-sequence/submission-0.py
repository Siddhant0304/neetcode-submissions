class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        s = set(nums)
        lis = sorted(list(s))

        maxCnt, cnt = 1,1

        for i in range(1,len(lis)):
            if lis[i]-lis[i-1]==1:
                cnt+=1
            else:
                maxCnt = max(maxCnt,cnt)
                cnt = 1
        
        maxCnt = max(maxCnt,cnt)
        return maxCnt