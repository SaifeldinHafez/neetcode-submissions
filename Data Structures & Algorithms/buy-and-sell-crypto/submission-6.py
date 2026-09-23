class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_day = 0
        sell_day = 1
        best_profit = 0

        if  len(prices) < 2:
            return 0

        for price in prices:
            profit = prices[sell_day] - prices[buy_day]
            best_profit = max(best_profit, profit)
            
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
                if sell_day != len(prices) - 1:
                    sell_day = buy_day + 1
            
            elif sell_day != len(prices) - 1:
                sell_day += 1
        
        return best_profit