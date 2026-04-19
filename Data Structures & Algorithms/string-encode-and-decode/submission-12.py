class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs == []:
            return ""

        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i] 
        
        return res
        
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            i = j + 1
            j = length + i 
            res.append(s[i:j])
            i = j
        return res 


        