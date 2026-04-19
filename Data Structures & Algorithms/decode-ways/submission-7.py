class Solution:
    def numDecodings(self, s: str) -> int:
        # double digit
        first = 0
        curr_dp = 0
        second = 1


        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr_dp = 0
            else:
                curr_dp = second 

            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                curr_dp += first
            second, first  =  curr_dp, second
        return second
    


