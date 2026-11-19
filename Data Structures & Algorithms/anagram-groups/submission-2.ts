class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        /*

        Make a hashmap, sort the string, check if in hashmap, if so append to list
        if not make a new one. Return the map

        */

        let freq = new Map<string, string[]>();

        for(const str of strs){
            let sorted = [...str].sort().join("")

            if(freq.has(sorted)){
                freq.get(sorted)!.push(str)
            }

            else{
                let boon = new Array<string>();
                boon.push(str)
                freq.set(sorted, boon)
            }
        }

        return Array.from(freq.values())





    }
}
