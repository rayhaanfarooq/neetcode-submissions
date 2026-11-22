class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        queue = deque()

        n = len(grid)
        m = len(grid[0])
        minutes = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    queue.append((row,col))


        while queue:
            size = len(queue)

            for _ in range(size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))

            minutes += 1

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    return -1

        return minutes - 1 if minutes > 0 else 0



        


        