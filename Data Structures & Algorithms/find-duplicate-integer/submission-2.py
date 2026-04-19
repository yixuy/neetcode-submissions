class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        fast = 0 
        slow = 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        # meet to next point
        slow_2 = 0

        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow 
