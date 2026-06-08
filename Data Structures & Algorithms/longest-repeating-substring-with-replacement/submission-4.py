class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        So the idea i
        The idea is to expand the window and keep track of the most occuring 
        char and then replace everything else so it is one char. This is the idea
        Keep track of hashmap and the most occuring element, if tie pick any letter
        maybe the first or most recent occuring? And then 

        So the hashmap has a dic of elements and for example if we know the 
        count is 8 A:4 and B:2 and C:2 and k then we need to check if the sum
        of the other elements is < k. This will give us the length of the longest string
        What our right pointer should just move but what about our left pointer.
        If the sum of the elements is more than k. So if we find a letter that isnt
        part of the largest group, then it becomes a replaced character. So keep doing this
        until you reach the end.

        Instead of summing its window length - most freq char. Everything else is garbae
        or replaceable


        '''
        

        l = 0
        r = 0
        count = {}
        max_len = 0
        currMax = None


        def counter(letter):
            nonlocal currMax
            if letter in count:
                count[letter] += 1
            
            else:
                count[letter] = 1


            if currMax is None:
                currMax = letter

            if count[letter] > count[currMax]:
                currMax = letter


        while r < len(s):
            #Track the elements
            counter(s[r])

            #Get the max element and set vars
           
            currLen = r - l + 1


            #Now compute for the replacements so window length - max
            #This computes the new longest repeating character
            if currLen - count[currMax] <= k:
                max_len = max(max_len,currLen)
                

            else:
                while currLen - count[currMax] > k:
                    count[s[l]] -= 1
                    l += 1
                    currLen = r - l + 1
                    currMax = max(count, key=count.get)
                    
                

            r += 1
            max_len = max(max_len, currLen)

        return max_len

            
            




            



            







        