class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''

        I got leetcode brained I didn't even fully solve the problem I just went off memory which is bad


        ok so I have two halves, one which is sorted and the other which isnt.

        if its sorted its regular binary search,

        if 



        '''



        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:

                if nums[l] <= target < nums[mid]:
                    r = mid - 1

                else:
                    l = mid + 1
            
            
            else:
                
                if nums[mid] < target <= nums[r]:
                    l = mid + 1

                else:
                    r = mid - 1
            
            


        return -1
        