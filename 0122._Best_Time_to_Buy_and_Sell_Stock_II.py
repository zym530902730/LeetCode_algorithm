class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            profit += prices[i] - prices[i - 1] if prices[i] - prices[i - 1] > 0 else 0
        return profit
