class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {


        let unique = new Set<string>();
        let left = 0
        let right = 0
        let max = 0


        for(const str of s){

            if(unique.has(str)){
                while(unique.has(str)){
                    unique.delete(s[left])
                    left++  
                }
            }

            
            unique.add(str)
            right += 1
            max = Math.max(max, right - left)
            

        

           
        }


        return max


    }
}
