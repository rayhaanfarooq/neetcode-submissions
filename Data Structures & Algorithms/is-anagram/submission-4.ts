class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {

        /*
        make two hashmaps and then compare each value
        */
         if (s.length !== t.length) return false;

        const map = new Map<string, number>();

        // Count characters in s
        for (const char of s) {
            map.set(char, (map.get(char) || 0) + 1);
        }

        // Subtract characters in t
        for (const char of t) {
            if (!map.has(char)) return false;

            map.set(char, map.get(char)! - 1);

            if (map.get(char) === 0) {
                map.delete(char);
            }
        }

        return map.size === 0;
    }



}

