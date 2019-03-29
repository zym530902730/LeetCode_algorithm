class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPrice = prices[0]
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return profit
