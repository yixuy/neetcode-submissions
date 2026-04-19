class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # if num == nums[i+1] and i < sort_nums.len() -1:
            #     continue
            if  i > 0 and num == nums[i-1] :
                continue

            first = i+1
            last =  len(nums) -1

            while first < last:
                if num + nums[first] + nums[last] == 0:
                    res.append([num, nums[first] , nums[last]])
                    # key keep doing 
                    first += 1
                    last -= 1
                    while nums[first] == nums[first-1] and first < last:
                        first += 1
                    
                elif num + nums[first] + nums[last] < 0:
                    first = first + 1
                else:
                    last = last - 1

        return res
            

        
        