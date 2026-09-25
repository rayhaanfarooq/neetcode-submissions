class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''

        there are three cases, 

        for example,

        we have an array of 3,4,5


        Find the inflection point
        so when the number is smaller then both the left and right element if they exist is the inflection. But how does one find the inflection?

        Ok so the idea is comparing the left and right pointers
        im lowkey a chud for not knowing I used to be a binary search
        demon.

        So the idea is to check order, if the left is smaller
        then we know that part is sorted and the min isnt there
        but if the right is smaller we know the min is there.
        Converse is true is larger is left then the min is left but if the larger is right ignore it. Only one can be true at a time so its doable.

        we can also keep track of the min so far, so thats probably the idea


        examples

        [1,2,3,4,5,6]

    
        [4,5,6,7]

        [9,-5,-2,0,3]

        '''

        smallest = float("inf")
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

    
        return nums[l]

        





        
        