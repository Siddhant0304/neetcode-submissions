from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        cnt = 0
        m,n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(i,j):
            if i<=-1 or j<=-1 or i>=m or j>=n or grid[i][j]=='0' or visited[i][j]==1: return
            visited[i][j]=1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    if visited[i][j]==0:
                        cnt+=1
                        dfs(i,j)
        return cnt


        

     
        



    

