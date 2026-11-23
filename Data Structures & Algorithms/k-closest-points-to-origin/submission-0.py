import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        '''
        Super easy, compute distance push to heap keep heap of size k


        '''
        heap = []

        for x,y in points:
            distance = sqrt(x**2 + y**2)

            heapq.heappush(heap, (-distance, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)


        result = []
        while heap:
            distance, points = heapq.heappop(heap)
            result.append(points)


        return result
