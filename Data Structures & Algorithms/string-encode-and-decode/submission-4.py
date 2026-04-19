class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "//"
        if len(strs) == 0:
            return "/"
        res = ""
        for str in strs:
            res = res + str + "/" 
        return res
        
    def decode(self, s: str) -> List[str]:
        if s == "//":
            return []
        if s == "/":
            return [""]
        # split the string by /
        
        return s.split("/")[:-1]