class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Ok so tradiontally just use a set. If in set return else add

        '''

        dupes = set()

        for num in nums:
            if num in dupes:
                return num
            
            else:
                dupes.add(num)

                

        