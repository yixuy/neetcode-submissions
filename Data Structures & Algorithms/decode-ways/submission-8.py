class Solution:
    def numDecodings(self, s: str) -> int:
        # double digit
        temp = 0
        first = 0
        second = 1


        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                first = 0
            else:
                first = second 

            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                first += temp
            second, temp  =  first, second
        return second
    


