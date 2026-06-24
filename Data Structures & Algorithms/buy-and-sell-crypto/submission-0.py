class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        # l=buy , r=sell

        max_profit = 0
        curr_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                l = r
            r += 1
            
        return max_profit
            
