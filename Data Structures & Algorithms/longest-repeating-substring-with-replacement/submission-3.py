class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}

        # form a freq map
        # for c in s:
        #     if c in freq:
        #         freq[c] += 1
        #     else:
        #         freq[c] = 0
        
        left = 0


        # count - most freq count compared with k

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
            # print(freq)
            if i - left + 1 - max(freq.values()) <= k:
                if i - left + 1 > res:
                    res = i - left + 1
            else:
                while i - left + 1 - max(freq.values()) > k:
                    freq[s[left]] -= 1
                    left += 1
            # if i - left + 1 > res:
            #     res = i - left + 1
        
        return res

        



     



            