class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''

        Start from the edges and work backwards. Check which cells reach
        the atlantic and which cells can reach the pacific. Then find the intersection
        of these two sets and you're done


        '''
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        n = len(heights)
        m = len(heights[0])

        pacific = set()
        atlantic = set()
        pacific_queue = deque()
        atlantic_queue = deque()


        #setup bfs
        def bfs(queue, visited):

            while queue:
                row,col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited and 
                    heights[nr][nc] >= heights[row][col]):

                        queue.append((nr,nc))
                        visited.add((nr,nc))


        #Setup pacific 
        for c in range(m):
            pacific_queue.append((0,c))
            pacific.add((0,c))

        for r in range(n):
            pacific_queue.append((r,0))
            pacific.add((r,0))

        #Setup atlantic 
        for c in range(m):
            atlantic_queue.append((n-1,c))
            atlantic.add((n-1,c))

        for r in range(n):
            atlantic_queue.append((r,m-1))
            atlantic.add((r,m-1))

        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)

        result = []

        for r in range(n):
            for c in range(m):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result











       

        