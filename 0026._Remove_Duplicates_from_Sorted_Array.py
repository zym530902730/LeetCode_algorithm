class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums == []:
            return 0
        n = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                n+=1
                nums[n] = nums[i+1]
        return n+1