from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        maxArea = 0
        n = len(grid)
        m = len(grid[0])

      


        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    queue = deque([(r,c)])
                    grid[r][c] = 0
                    currArea = 1

                    while queue:
                        row, col = queue.popleft()

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                currArea += 1
                                queue.append((nr,nc))
                            
                            
                    
                    maxArea = max(maxArea, currArea)

            



        return maxArea

        