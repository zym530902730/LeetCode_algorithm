"""
思路： 跟3 Sum一样，固定一个元素
时间复杂度: O(N^2)******- 空间复杂度: O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return null

        nums = sorted(nums)
        closestNum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closestNum - target):
                    closestNum = threeSum
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return target
        return closestNum