class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #         if not nums:
        #             return False
        #         set1=list(set(nums))

        #         return not len(set1) == len(nums)

        k = set()
        for i in nums:
            if i in k:
                return True
            else:
                k.add(i)
        return False