class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights : return []
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r,c,ocean, prev_height):
            if r<=-1 or r>=m or c<=-1 or c>=n or (r,c) in ocean or heights[r][c] < prev_height: return 
            ocean.add((r,c))

            dfs(r-1,c,ocean, heights[r][c])
            dfs(r+1,c,ocean, heights[r][c])
            dfs(r,c-1,ocean, heights[r][c])
            dfs(r,c+1,ocean, heights[r][c])

        for i in range(m):
            dfs(i,0,pacific, heights[i][0])
            dfs(i,n-1,atlantic, heights[i][n-1])
        
        for j in range(n):
            dfs(0,j, pacific, heights[0][j])
            dfs(m-1,j, atlantic,heights[m-1][j])
       
        print(atlantic)
        print(pacific)
        common = [list(sub) for sub in pacific if sub in atlantic]
        return common


        