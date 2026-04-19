class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != 0 and len(s) == len(t):
            count_s = {}
            count_t = {}
            
            for i in range(len(s)):
                count_s[s[i]] =  count_s.get(s[i], 0)+ 1
                count_t[t[i]] =  count_t.get(t[i], 0) + 1

            for c in count_s:
                if count_s.get(c) != count_t.get(c):
                    return False
            return True

        return False;
            