class Solution:
    def numDecodings(self, s: str) -> int:
        # double digit
        temp = 0
        first = 0
        second = 1


        for i in range(len(s) - 1, -1, -1):
            # check single character
            if s[i] == "0":
                curr = 0
            else:
                curr = second 
            #  check multiple character
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                curr += first
            second, first  =  curr, second
        return second
    


