from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        n = len(board)
        m = len(board[0])

        queue = deque()
        visited = set()

        
        for c in range(m):
            if board[0][c] == "O":
                queue.append((0,c))
                visited.add((0,c))

            if board[n - 1][c] == "O":
                queue.append((n - 1, c))
                visited.add((n-1, c))
        
        for r in range(n):
            if board[r][0] == "O":
                queue.append((r, 0))
                visited.add((r,0))

            if board[r][m - 1] == "O":
                queue.append((r,m - 1))
                visited.add((r, m-1))

        while queue:
            row, col = queue.popleft()


            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O" and (nr,nc) 
                not in visited):
                    queue.append((nr,nc))
                    visited.add((nr,nc))

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

            


        


        