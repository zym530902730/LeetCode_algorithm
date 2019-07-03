<<<<<<< HEAD
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
=======
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
>>>>>>> bebc8612da16ca8e407398a44eba42627767ace0
        return False