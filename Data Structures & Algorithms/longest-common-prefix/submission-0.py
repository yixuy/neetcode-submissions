class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        mapping = {}

        for s in strs:
            for i in range(len(s)):
                mapping[(s[i], i)] = mapping.get((s[i], i), 0) + 1
        count = 0
        for key, val in mapping.items():
            if val == len(strs) and key[1] == count:
                res += key[0]
                count += 1
            else:
                break

        return res
             
        