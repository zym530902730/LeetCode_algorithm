class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        left = 0
        up = 0
        down = n - 1
        right = n - 1

        count = 0
        direction = 0
        res = [[0 for _ in range(n)] for _ in range(n)]

        while True:
            if direction == 0:
                # turn right
                for i in range(left, right + 1):
                    count += 1
                    res[up][i] = count
                up += 1
            elif direction == 1:
                # turn down
                for i in range(up, down + 1):
                    count += 1
                    res[i][right] = count
                right -= 1
            elif direction == 2:
                # turn left
                for i in range(right, left - 1, -1):
                    count += 1
                    res[down][i] = count
                down -= 1
            else:
                # turn up
                for i in range(down, up - 1, -1):
                    count += 1
                    res[i][left] = count
                left += 1

            direction = (direction + 1) % 4
            if count >= n * n:
                return res





# 网络答案，太精巧，想不到
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        l = n * n + 1
        while l > 1:
            l, r = l - len(res), l
            res = [list(range(l, r))] + list(zip(*res[::-1]))
        return res