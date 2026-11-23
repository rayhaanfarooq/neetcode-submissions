from heapq import heapify_max, heappush_max, heappop_max
'''
Take a heap, keep it size of min, min is kth

'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def kthLargest(self):
        return self.heap[0]

        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.kthLargest()
        

        
