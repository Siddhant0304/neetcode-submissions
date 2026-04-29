from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #using Topo sort (BFS)
        adjList = [[] for _ in range(numCourses)]
        in_degree = [0]*numCourses 
        res = []
        for preq in prerequisites:
            adjList[preq[1]].append(preq[0])
            in_degree[preq[0]]+=1
        
        q= deque([i for i in range(numCourses) if not in_degree[i]])
        count = 0

        while q:
            temp = q.pop()
            res.append(temp)
            count+=1
            for k in adjList[temp]:
                in_degree[k]-=1
                if in_degree[k]==0: q.appendleft(k)
        
        print(res) #sequence of doing course
        return count==numCourses



        




        # using DFS
        # adjList = [[] for _ in range(numCourses)]
        # for preq in prerequisites:
        #     adjList[preq[1]].append(preq[0])

        # visited= [0] * numCourses
        # pathVisited = visited.copy()

        # def dfs(node):
        #     if pathVisited[node] == 1: return True
        #     if visited[node]==1 and pathVisited[node]==0 : return False
        #     visited[node], pathVisited[node]=1,1

        #     for k in adjList[node]:
        #         if dfs(k) == True: return True

        #     pathVisited[node] = 0
        #     return False

        # for i in range(numCourses):
        #     if visited[i]==0:
        #         if dfs(i) == True: return False
        
        # return True
      
     
        

    
                   
        


        
       

       




        