class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            # 相对从中后段开始，较慢
            # mid = (r + l) //2
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[l] > target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1