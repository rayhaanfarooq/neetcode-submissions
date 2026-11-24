import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

        for key in freq:
            heapq.heappush(heap, (freq[key], key))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for _ in range(len(heap)):
            value,key = heapq.heappop(heap)
            result.append(key)

        return result


        


        