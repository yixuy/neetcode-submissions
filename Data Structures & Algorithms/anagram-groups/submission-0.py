class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a tuple as the key for the hashmap, the value is the list of Anagrams 
        res = defaultdict(list)

        for s in strs:
            # create a list of character
            count = [0] * 26 
            # get the count map
            for c in s:
                count[ord(c) -  ord('a')] += 1 

            res[tuple(count)].append(s)
            print(res)
        return res.values()


            
        
        

            
        
        