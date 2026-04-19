class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.res = ""
        def check_palindrome(left, right):
         

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 2 + 1 > len(self.res):
                self.res = s[left + 1 : right ]
                
        for i in range(len(s)):
            check_palindrome(i, i)
            check_palindrome(i, i + 1) 
        
        return self.res