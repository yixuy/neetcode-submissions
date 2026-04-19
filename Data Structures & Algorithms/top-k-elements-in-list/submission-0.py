class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        # sort the nums 
        sort_nums = nums.sort()
        
        res_map = {}
        for num in nums:
            res_map[num] = res_map.get(num, 0) + 1 
          
        # find the top k value in hashmap
        # sort by value
        sort_value = dict(sorted(res_map.items(), key = lambda item: item[1], reverse = True))
        res = []

        # for i in range(k):
        #     res.append(sort_value.value())
        value_list = list(sort_value.keys()) 

        return value_list[:k]




        