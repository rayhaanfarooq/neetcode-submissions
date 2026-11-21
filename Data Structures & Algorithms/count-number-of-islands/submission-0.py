from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
        Run bfs
        count islands
        '''


        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        n = len(grid)
        m = len(grid[0])
        islands = 0


        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    islands += 1

                    queue = deque([(r,c)])
                    grid[r][c] = "0"

                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nr = dr + row
                            nc = dc + col

                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr,nc))


                




                
        return islands





        
        