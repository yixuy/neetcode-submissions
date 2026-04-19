class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # In s no 
        
        unordered_map = dict()

        for c in t:
            unordered_map[c] = 1+ unordered_map.get(c, 0)

        
        min_len = len(s)
        res = ""
        for i, c in enumerate(s):
            if c in unordered_map:
                temp_i = i
                hash_map = dict()
                while temp_i < len(s):
                    if s[temp_i] in unordered_map:
                        hash_map[s[temp_i]] = 1+ hash_map.get(s[temp_i], 0)
                        if len(hash_map) == len(unordered_map) and min_len >= temp_i - i:
                            check = True 
                            print(hash_map)
                            for key, value in unordered_map.items():
                                if hash_map[key] < unordered_map[key]:
                                    check = False
                            if check:
                                min_len = temp_i - i + 1
                                res = s[i: temp_i+1]
                                break
                    temp_i += 1
        return res