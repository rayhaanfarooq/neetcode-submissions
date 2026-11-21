class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        result += nums1
        result += nums2

        result = sorted(result)

        if len(result) % 2 == 0:
            index1 = len(result) // 2 - 1
            index2 = len(result) // 2 
            total = (result[index1] + result[index2]) / 2
            return total
        
        else:
            index = len(result) // 2
            return result[index]


        

        