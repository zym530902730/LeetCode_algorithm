class Solution:
    def canWinNim(self, n: int) -> bool:
        """
            堆中石头数量不能被n整除，可以赢得胜利
        """

        return not (n % 4 == 0)