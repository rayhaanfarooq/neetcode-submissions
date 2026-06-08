class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       news = "".join(sorted(s))
       newt = "".join(sorted(t))

       return news == newt

  
        
        

       
        