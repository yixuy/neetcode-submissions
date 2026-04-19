class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # repeat?

        # using set  
        num_set = set(nums)
        longest = 0
        # 1 2 3 4 100 200
        # create a new set
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while (length + num) in num_set:
                    length += 1
                
                longest = max(length, longest)
        return longest

        