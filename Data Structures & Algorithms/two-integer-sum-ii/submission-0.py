class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''

        Use two points one on each end.
        If sum is larger then two points move right pointer
        if sum is smaller then two points move left pointer

        '''

        l = 0
        r = len(numbers) - 1

        while l < r:

            currSum = numbers[l] + numbers[r]

            if currSum == target:
                return [l + 1, r + 1]

            elif currSum > target:
                r -= 1

            else:
                l += 1

        
        