class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        
        for s in strs:
            temp = ''.join(sorted(s))
            mapping[temp].append(s)
        

        return list(mapping.values())