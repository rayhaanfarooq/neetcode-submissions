class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        '''
        The idea is that, given an anagram, the sorting of the letters 
        will always be the same so we can run sort on a string or even anagrams
        both will probably take O(n) time to solve so its ok. So what we do
        is for every word sort the word check if it exists, if it does then append it to the array
        the structure will look like this:

        word: list of words

        Note, for the initializing of every key ensure that the word itself is the starting word
        For every other word it is fine. Then for the answer you would do
        dict.values which should return all the lists in one big list.


        '''

        tracker = {}

        for word in strs:
            sort = "".join(sorted(word))

            if sort in tracker:
                tracker[sort].append(word)

            else:
                tracker[sort] = [word]

        

        return list(tracker.values())
        
        


        