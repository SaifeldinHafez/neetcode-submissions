class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        lowest_price = prices[0]

        for price in prices:
            lowest_price = min(price, lowest_price)
            best_profit = max(best_profit, price - lowest_price)
        return best_profit