class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if nums == []:
        #     return []
        # # sort the list
        # sort_nums = nums.sort()
        # res_map = {}
        # for num in nums:
        #     res_map[num] = res_map.get(num, 0) + 1 
          
        # # find the top k value in hashmap
        # # sort by the map
        # sort_value = dict(sorted(res_map.items(), key = lambda item: item[1], reverse = True))
        # res = []
        # # get the list
        # value_list = list(sort_value.keys()) 
        # return value_list[:k]


        # bucket sort
        # make a count bucket and value
        count = {}
        freq = [[]for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # create freq bucket
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res
        return res

        