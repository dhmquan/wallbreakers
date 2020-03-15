from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        #track in-degree for topological sort
        for y, x in prerequisites:
            graph[x].append(y)
            in_degree[y] += 1
            
        q = deque()
        for y in range(numCourses):
            if in_degree[y] == 0:
                q.append(y)
                
        #run BFS from nodes with 0 in-degrees
        seen = 0
        while q:
            node = q.popleft()
            seen += 1
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                    
        return seen == numCourses