class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        Slide over array with the set, add letters to set.
        Once a letter is reached in the array that is in the set,
        Shrink from the left until it the letter duped is gone
        When adding a letter update the maximum.
        '''

        max_length = 0
        dupes = set()
        l = 0
        r = 0


        while r != len(s):
            if s[r] not in dupes:
                dupes.add(s[r])
                max_length = max(max_length, len(dupes))
                r += 1

            else:
                while s[r] in dupes:
                    dupes.remove(s[l])
                    l += 1

            


        return max_length

        