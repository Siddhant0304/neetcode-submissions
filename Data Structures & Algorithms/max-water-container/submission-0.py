class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxarea = 0
        cur = 0

        i,j = 0, n-1

        while i < j:
            cur = min(heights[i],heights[j])*(j-i)
            maxarea = max(maxarea, cur)
            if heights[i] <= heights[j]: i+=1
            else: j-=1

        return maxarea


        