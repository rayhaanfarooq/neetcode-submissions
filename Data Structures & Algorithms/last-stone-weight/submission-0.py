import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -stone)


        while len(heap) > 1:
            largest = heapq.heappop(heap)
            secondLargest = heapq.heappop(heap)

            if largest == secondLargest:
                continue

            else:
                new = secondLargest - largest
                heapq.heappush(heap, -new)


        result = 0

        if len(heap) == 1:
            return -heapq.heappop(heap)


        return 0


        


        