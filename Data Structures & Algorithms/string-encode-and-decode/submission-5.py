class Solution:

    def encode(self, strs: List[str]) -> str:
        # empty and str with length is 0 
        # if strs == []:
        #     return "//"
        # if len(strs) == 0:
        #     return "/"
        # res = ""
        # for str in strs:
        #     res = res + str + "/" 
        # return res

        # encode  + len(str) + "/"
        
        res = ""

        for s in strs:
            res += str(len(s)) + "/" + s
        return res

        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '/':
                j = j + 1
            
            s_len = int(s[i:j])
            i = j + 1
            j = i + s_len
            res.append(s[i:j])
            i = j

        return res

        # if s == "//":
        #     return []
        # if s == "/":
        #     return [""]
        # return s.split("/")[:-1]