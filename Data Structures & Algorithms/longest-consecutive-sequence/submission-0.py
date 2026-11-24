class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Get a set of nums to remove dupes and for O(1) checking
        numSet = set(nums)
        longest = 0


        #Loop through the array
        for num in nums:

            #The idea is, find the start. If the one before it exists
            #Then it isnt the start of the aray
            if (num - 1) not in numSet:
                #Initialize the starting length, any sequence will always have
                #minimum 1 length
                length = 1

                #This is the core of the logic, keep checking if every consecutive number
                #Exists, once you're out, return the longest
                while(num + length) in numSet:
                    length += 1

                longest = max(length, longest)


        
        return longest
            






        

        
        