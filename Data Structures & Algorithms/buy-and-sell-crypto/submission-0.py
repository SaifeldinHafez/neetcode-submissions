class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if (prices[j] - prices[i]) > highest_profit:
                    highest_profit = prices[j] - prices[i]
        
        return highest_profit