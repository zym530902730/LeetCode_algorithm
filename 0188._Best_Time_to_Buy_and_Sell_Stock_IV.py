class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        """
            应用动态规划的思想：
            问题划分为在 i 天之前和之后两部分
            min 最低买入价
            max 最高卖出价
            profit_l[i] = max(profit_l[i-1], prices[i] - min)
            profit_r[i] = max(profit_r[i+1], max - prices[i])

        """
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