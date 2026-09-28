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

        # O(M) time where m = len(s1)
        s1Freq = Counter(s1)
        window = Counter()
        m = len(s1)

        for i in range(len(s2)):

            window[s2[i]] += 1

            if i >= m:
                left_char = s2[i - m]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]



    
            if s1Freq == window:
                return True


        return False

        

        