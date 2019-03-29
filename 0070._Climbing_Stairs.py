class Solution:
    cache = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]