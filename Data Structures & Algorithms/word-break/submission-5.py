class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        word_set = set(wordDict)
        max_word = 0
        
        for word in word_set:
            max_word = max(len(word), max_word)

        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            memo[i] = False 
            for j in range(i, min(len(s), i + max_word)):
                if s[i:j+1] in word_set:
                    if dp(j+1):
                        memo[i] = True
                        return True

            return memo[i]

        return dp(0)
