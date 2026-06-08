class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Two pointer solution
        # 7 x 6
        # So start two pointers
        # So start, increment one, calculate total area. Move again.
        #We want to keep track of the largest one so far.
        #Take the min of the two
        #If the next one is larger then the first. move the first pointer
        #Else move the second pointer

        total_area = 0
        l = 0
        r = len(heights) - 1

    
        while l < r:
            new_area = min(heights[l], heights[r]) * (r - l)
            total_area = max(total_area, new_area)

            if heights[l] > heights[r]:
                r -= 1

            else:
                l += 1

        return total_area




        