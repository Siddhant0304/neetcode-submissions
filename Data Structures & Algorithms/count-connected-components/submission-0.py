from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        visited = [0]*n
        count = 0

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        def bfs(node):
            q= deque()
            q.appendleft(node)
            
            while q:
                temp = q.pop()
                visited[temp] = 1
                for k in adjList[temp]:
                    if not visited[k]:
                        q.appendleft(k)



        for k in range(n):
            if visited[k] == 0:
                count+=1
                bfs(k)


        return count


        