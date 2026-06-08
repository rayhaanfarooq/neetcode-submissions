class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        unique = {}

        for i in range(0, len(nums)):
            unique[nums[i]] = i


        for i in range(0, len(nums)):
            need = target - nums[i]

            if need in unique and unique[need] != i:
                return sorted([unique[need], i])
        