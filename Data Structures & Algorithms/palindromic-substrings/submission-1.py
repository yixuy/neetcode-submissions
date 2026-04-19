class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return 1
        def countPalindromic(s, left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        res = 0
        for i in range(len(s)):
            res += countPalindromic(s, i, i)
            res += countPalindromic(s, i, i+1)

        return res
        