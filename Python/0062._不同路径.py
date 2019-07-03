class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #         # C(m+n-2, m-1)
        #         if m == 0 or n == 0:
        #             return 0
        #         if m == 1 and n ==1:
        #             return 1

        #         return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        if m < 1 or n < 1:
            return 0
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]