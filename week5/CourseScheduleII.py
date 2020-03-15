from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for y, x in prerequisites:
            graph[x].append(y)
            in_degree[y] += 1
          
        #start with nodes with 0 in-degree
        q = deque()
        for y in range(numCourses):
            if in_degree[y] == 0:
                q.append(y)
                
        #run topological sort
        out = []
        while q:
            v = q.popleft()
            out.append(v)
            
            for neighbor in graph[v]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                    
        if len(out) != numCourses:
            return []
        
        return out