
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = [[] for _ in range(numCourses)]
        for preq in prerequisites:
            adjList[preq[1]].append(preq[0])

        visited= [0] * numCourses
        pathVisited = visited.copy()

        def dfs(node):
            if pathVisited[node] == 1: return True
            if visited[node]==1 and pathVisited[node]==0 : return False
            visited[node], pathVisited[node]=1,1

            for k in adjList[node]:
                if dfs(k) == True: return True

            pathVisited[node] = 0
            return False

        for i in range(numCourses):
            if visited[i]==0:
                if dfs(i) == True: return False
        
        return True
      
     
        

    
                   
        


        
       

       




        