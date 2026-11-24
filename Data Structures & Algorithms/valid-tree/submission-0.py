class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        '''
        This is just a cycle detection. So go through the entire thing and check
        for 1) cycles and 2) any disconnted components
        We can use dfs? With the state? 

        So actually I can check if the edges are n-1, if its ones more then theres a
        cycle if its less then its disconnected. So yo uneed to check edges + if its
        disconnected.


        '''

        graph = {i : [] for i in range(n)}

        for path1, path2 in edges:
            graph[path1].append(path2)
            graph[path2].append(path1)

        if len(edges) != n - 1:
            return False


        visited = set()


        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        
        dfs(0)

        return len(visited) == n

            



















        