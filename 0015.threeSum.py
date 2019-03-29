<<<<<<< HEAD
"""
时间复杂度: O(N^2) 空间复杂度: O(N)

排序
固定左边，如果左边重复，继续
左右弄边界，去重，针对不同的左右边界情况处理

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        elif nums[0] == 0 and nums[-1] == 0:
            return [[0, 0, 0]]

        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif target < nums[j] + nums[k]:
                    k -= 1
                else:
                    j += 1
=======
"""
时间复杂度: O(N^2) 空间复杂度: O(N)

排序
固定左边，如果左边重复，继续
左右弄边界，去重，针对不同的左右边界情况处理

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        elif nums[0] == 0 and nums[-1] == 0:
            return [[0, 0, 0]]

        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif target < nums[j] + nums[k]:
                    k -= 1
                else:
                    j += 1
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
        return result