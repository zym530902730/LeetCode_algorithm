"""
    总方向呈 → ↓ ← ↑
    考虑使用四个变量维护方向

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left = 0
        up = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1

        # 0 -> right, 1 -> down, 2-> left, 3 -> up
        direction = 0
        res = []
        while True:
            if left > right or up > down:
                return res
            elif direction == 0:  # go right
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
                direction = 1
            elif direction == 1:  # go down
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
                direction = 2
            elif direction == 2:  # go left
                for i in reversed(range(left, right + 1)):
                    res.append(matrix[down][i])
                down -= 1
                direction = 3
            else:  # go up
                for i in reversed(range(up, down + 1)):
                    res.append(matrix[i][left])
                left += 1
                direction = 0
            if up > down or left > right:
                return res
