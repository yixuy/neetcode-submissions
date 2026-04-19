class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = {}

        for c in s:
            mapping[c] = mapping.get(c, 0) + 1

        for c in t:
            if c not in mapping:
                return False
            if mapping[c] <= 0:
                return False
            mapping[c] = mapping.get(c, 0) - 1

        for value in mapping.values():
            if value != 0:
                return False
        return True
            