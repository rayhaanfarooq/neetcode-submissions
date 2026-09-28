from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        So if len(s1) > len(s2) return false

        Now the main algortihm

        Keep window the size of s1

        Hashmap to track occurance

        Move window up, once window is max size,
        move left pointer up,

        '''

        if len(s1) > len(s2):
            return False

        s1Freq = {}
        window = []

        for char in s1:
            if char in s1Freq:
                s1Freq[char] +=1 
            
            else:
                s1Freq[char] = 1

        
        print(s1Freq)

        for char in s2:

            if len(window) == len(s1):
                window.pop(0)

            
            
            window.append(char)
            occurance = Counter(window)
    
            if s1Freq == occurance:
                return True


        return False

        