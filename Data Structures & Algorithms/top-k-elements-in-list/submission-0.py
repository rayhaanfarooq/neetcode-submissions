import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        To solve this you need heaps, and you would pop until you get k elements in the array

        But the optimized version is suing quick select which is something that I would like to learn
        Ok so this is just nlogk.

        So you iterate through the list get your freq and then pop it all onto it max heap.


        '''

        #Step 1) Setup the counts
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1

            else:
                counter[num] = 1


        #(priority, value)
        #Step 2) Add to heap

        max_heap = []

        for key in counter:
            max_heap.append((counter[key], key))

        heapq.heapify_max(max_heap)

        # Remove from heap
        # Here we want to essentially remove k elements, so when we pop
        #We want to append the second element until k elements are stored

        result = []

        for i in range(k):
            num = heapq.heappop_max(max_heap)
            result.append(num[1])
            

        return result

        #This runs in nlogk time with O(n) space. The optimized solution is
        # to use quick select but this is a decently advanced alg to memorize
        # and type out on the spot


        

        