class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Ok so tradiontally just use a set. If in set return else add


        ok so what if we used a sum? Expected sum vs real sum that difference
        is the duped integer

        Binary search? Well what if we did actual sum vs predicted sum



        '''

        slow = nums[0]
        fast = nums[nums[0]]



        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]


        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

            

        

        


        



        