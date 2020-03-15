from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for v in range(len(graph)):
            if v in colors:
                continue
            if not self.bfs(graph, v, colors):
                return False
        return True
    
    #run bfs from a node
    def bfs(self, graph, root, colors):
        q = deque()
        q.append((root, 0))
        
        while q:    
            v, parent_color = q.popleft()
            
            #if node has been visited, make sure its color differs from parent's color
            if v in colors:
                if colors[v] == parent_color:
                    return False
                continue
                
            colors[v] = 1 - parent_color
            for neighbor in graph[v]:
                q.append((neighbor, colors[v]))
                
        return True