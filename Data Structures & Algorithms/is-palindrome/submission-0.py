import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        temp_s = re.sub(r'\W+', '', s)
        temp_s = temp_s.replace(" ", "")
        last = len(temp_s) - 1
        while first < last:
            if temp_s[first].lower() == temp_s[last].lower():
                first = first + 1
                last = last - 1 
            else:
                return False
        return True