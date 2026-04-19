class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # sliding window
        # hash map 
        if len(s1) > len(s2):
            return False
        s1_count = {}
        s2_count = {}
        len_s1 = len(s1) 

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        for i in range(len_s1):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        if s1_count == s2_count:
            return True
        for i in range(len_s1, len(s2)):
            s2_count[s2[i-len_s1]] -= 1
            # it will check the dictionary, so you need to delete
            if s2_count[s2[i-len_s1]] == 0:
                del s2_count[s2[i-len_s1]]
            
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            if s1_count == s2_count:
                return True
        return False








        
            