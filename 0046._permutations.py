"""
递归
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for n in nums:
            prefix  = nums+[] # 硬拷贝
            prefix .remove(n)
            #prefix = nums[i]
            #prefix = nums[:i] + nums[i+1:]
            for m in self.permute(prefix ):
                res.append([n] + m)
        return res