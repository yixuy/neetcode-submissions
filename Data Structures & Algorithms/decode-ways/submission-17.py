class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s) 
        # if 1 <= int(s[len(s) - 1]) <= 9:
        #     memo[len(s) - 1] = 1
        # else:
        #     memo[len(s) - 1] = 0
        # 1 2 3 
        # 1 2 3 
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if memo[i] != -1:
                return memo[i]

            res = dfs(i+1)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26 :
                    res += dfs(i+2)
            memo[i] = res
            return memo[i]

        return dfs(0)