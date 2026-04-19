class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0
        right = 1
        cur_profit = 0
        
        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            
            if cur_profit > res:
                res = cur_profit
            if cur_profit < 0:
                left = right 
                cur_profit = 0
            right += 1

        return res