class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy shift the goal

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal -= nums[i]
                print(goal)
         
        if goal > 0 or (len(nums) > 1 and goal == 0 and nums[goal] == 0):
            return False
        
        return True





