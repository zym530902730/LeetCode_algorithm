class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxKProfit(K, prices):
            if K >= len(prices) // 2:
                return sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)])
            if not prices or len(prices) == 0:
                return 0
            dp, min_ = [0] * (K + 1), [prices[0]] * (K + 1)
            for i in range(1, len(prices)):
                for k in range(1, K + 1):
                    min_[k] = min(min_[k], prices[i] - dp[k - 1])
                    dp[k] = max(dp[k], prices[i] - min_[k])
            return dp[-1]

        return maxKProfit(2, prices)
