<<<<<<< HEAD
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = m = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            if curr_sum > m:
                m = curr_sum
        return m
=======
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = m = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            if curr_sum > m:
                m = curr_sum
        return m
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
