class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        # contain one character
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[r])
            res = max(res, r-left+1)
            
        return res
            