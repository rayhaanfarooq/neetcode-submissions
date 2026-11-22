class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        This is different from max area of island + number of islands
        as this is multi start bfs.

        We wanna start queue with all the nodes, run until the end of the thing
        so we can queue up every sequential node. Mark them with a var, then add their
        nearby nodes mark them with a var so on so forth.
        '''

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        distance = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            size = len(queue)

            for _ in range(size):
                row, col = queue.popleft()
                
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                   
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = distance + 1
                        queue.append((nr,nc))
                
            distance += 1


           

            

        
        