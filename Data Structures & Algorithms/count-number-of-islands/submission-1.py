from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        cnt = 0
        m,n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def bfs(i,j): #try with bfs
            q = deque()
            q.appendleft((i,j))

            while q:
                temp = q.pop()
                visited[temp[0]][temp[1]]=1
                direction = [(-1,0),(1,0),(0,-1),(0,1)]
                for dx,dy in direction:
                    currX, currY = temp[0]+dx, temp[1]+dy
                    if currX >-1 and currX < m and currY >-1 and currY < n and visited[currX][currY]==0 and grid[currX][currY]=="1":
                        q.appendleft((currX, currY))

                        
        # def dfs(i,j): #dfs works fine
        #     if i<=-1 or j<=-1 or i>=m or j>=n or grid[i][j]=='0' or visited[i][j]==1: return
        #     visited[i][j]=1
        #     dfs(i-1,j)
        #     dfs(i+1,j)
        #     dfs(i,j-1)
        #     dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==0:
                    cnt+=1
                    bfs(i,j)
        return cnt


        

     
        



    

