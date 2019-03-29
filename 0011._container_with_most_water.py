class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            if b * h > maxArea:
                maxArea = b * h
        return maxArea