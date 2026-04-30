class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = [[] for _ in range(n)]

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = [0]*n

        def dfs(node, parent):
            visited[node]=1
            for k in adjList[node]:
                if not visited[k]:
                    if dfs(k,node)==True: return True
                else:
                    if k != parent: return True
                
            return False

        if dfs(0,-1)== True: return False
        for k in range(n):
            if visited[k]==0: return False
        print(visited)
        return True

             
            

        
        