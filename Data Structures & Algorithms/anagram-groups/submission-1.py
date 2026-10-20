class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        '''

        The idea is to take a dictionary, map a key to array of values. Make sure to sort the word first and then add it




        '''


        freq = {}

        for word in strs:
            key = str(sorted(word))
            if key in freq:
                freq[key].append(word)

            else:
                freq[key] = [word]



        return list(freq.values())


        