class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        I need to find the number of connected component. Now one way I can do this
        is make dfs, put all in a visited set, increment by one. I need to run dfs
        on multiple disconnected nodes. 
        '''


        graph = {i : [] for i in range(n)}
        
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)

        visited = set()
        count = 0
        

        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

    
            
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
                
            
        return count

            











        